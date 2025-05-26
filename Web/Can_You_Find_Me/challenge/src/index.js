const express = require('express');
const { engine } = require('express-handlebars');
const puppeteer = require('puppeteer');
const app = express();
const path = require('path');

app.engine('hbs', engine({ extname: '.hbs', defaultLayout: false }));
app.set('view engine', 'hbs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.render('index', { title: 'Create your own webpages!' });
});

app.post('/generate', (req, res) => {
    const userInput = req.body.input || '';
    const pageId = Date.now().toString();
    res.redirect(`/page/${pageId}?input=${encodeURIComponent(userInput)}`);
});

app.get('/page/:id', (req, res) => {
    const pageId = req.params.id;
    const userInput = req.query.input || '';
    res.render('generated', { userInput, pageId });
});

app.get('/adminbot', async (req, res) => {
    const targetUrl = req.query.url;

    console.log(`Admin bot visiting: ${targetUrl}`);

    try {
        const browser = await puppeteer.launch({
            headless: 'new',
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        const page = await browser.newPage();

        await page.setCookie({
            name: 'flag',
            value: 'WSUCTF{f4k3_flag}',
            domain: 'waynestateuniversity-ctf24-handlebars.chals.io', // if running locally, replace with localhost or docker interface ip
            path: '/',
            httpOnly: false,
        });

        await page.goto(targetUrl, { waitUntil: 'networkidle2', timeout: 5000 });
        await browser.close();

        res.send('Admin bot has visited the page');
    } catch (err) {
        console.error('Admin bot error:', err);
        res.status(500).send('Error running admin bot');
    }
});

app.listen(3000, () => {
    console.log('CTF server running on port 3000');
});
