using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Security.Cryptography;
using System.Text;


namespace Server
{
    class Program
    {
        static void Main(string[] args)
        {

            string actualPassphrase = "WayneStateUniversity";
            
            Console.WriteLine("CTF Server starting... Enter passphrase to unlock the flag:");
            string passphrase = Console.ReadLine();

            string encryptedFlagBase64= "3lDcCgY1sQU7A6ffpdhqeBMBSf5hYGPE1xrpl6DGTssUGBhFxfeq4aJ2Tjtwl1xW7qFjLepeS6A2tVY9IA0rIQ==";

            if(passphrase != actualPassphrase){
                Console.WriteLine("I won't bother decrypting the flag, the passphrase is wrong.");
                return;
            }

            try
            {
                string flagPart1 = DecryptFlag(encryptedFlagBase64, passphrase);
                Console.WriteLine($"Flag Unlocked: {flagPart1}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Passphrase incorrect: {ex.Message}");
                return;
            }
        }

        static string DecryptFlag(string encryptedFlagBase64, string passphrase)
        {
            byte[] salt = Encoding.UTF8.GetBytes("FixedSalt12345678");
            using (var pbkdf2 = new Rfc2898DeriveBytes(passphrase, salt, 10000, HashAlgorithmName.SHA256))
            {
                byte[] key = pbkdf2.GetBytes(32); // 256-bit key
                byte[] iv = pbkdf2.GetBytes(16);  // 128-bit IV
                using (var aes = Aes.Create())
                {
                    aes.Key = key;
                    aes.IV = iv;
                    aes.Mode = CipherMode.CBC;
                    aes.Padding = PaddingMode.PKCS7;

                    byte[] encryptedFlag = Convert.FromBase64String(encryptedFlagBase64);
                    using (var decryptor = aes.CreateDecryptor())
                    using (var ms = new MemoryStream())
                    {
                        using (var cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Write))
                        {
                            cs.Write(encryptedFlag, 0, encryptedFlag.Length);
                            cs.FlushFinalBlock();
                        }
                        byte[] decrypted = ms.ToArray();
                        string base64Flag = Encoding.UTF8.GetString(decrypted);
                        return Encoding.UTF8.GetString(Convert.FromBase64String(base64Flag));
                    }
                }
            }
        }

        // Utility method to encrypt flag during development
        static string EncryptFlag(string flag, string passphrase)
        {
            string base64Flag = Convert.ToBase64String(Encoding.UTF8.GetBytes(flag));
            byte[] salt = Encoding.UTF8.GetBytes("FixedSalt12345678");
            using (var pbkdf2 = new Rfc2898DeriveBytes(passphrase, salt, 10000, HashAlgorithmName.SHA256))
            {
                byte[] key = pbkdf2.GetBytes(32);
                byte[] iv = pbkdf2.GetBytes(16);
                using (var aes = Aes.Create())
                {
                    aes.Key = key;
                    aes.IV = iv;
                    aes.Mode = CipherMode.CBC;
                    aes.Padding = PaddingMode.PKCS7;

                    byte[] plainBytes = Encoding.UTF8.GetBytes(base64Flag);
                    using (var encryptor = aes.CreateEncryptor())
                    using (var ms = new MemoryStream())
                    {
                        using (var cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
                        {
                            cs.Write(plainBytes, 0, plainBytes.Length);
                            cs.FlushFinalBlock();
                        }
                        return Convert.ToBase64String(ms.ToArray());
                    }
                }
            }
        }
    }
}