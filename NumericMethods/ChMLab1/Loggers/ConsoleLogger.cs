using System;
using System.Collections.Generic;
using System.Text;
using ChMLab1.Interfaces;

namespace ChMLab1
{
    class ConsoleLogger : ILogger
    {
        public ConsoleLogger() { }
        public void Log(string s)
        {
            Console.WriteLine(s);
        }
        public void Log(List<double> l)
        {
            foreach(double d in l)
            {
                Console.Write("|{0,22}", d);
            }
            Console.WriteLine();
        }
        public void Log(params object[] list)
        {
            var s = "";
            foreach (object o in list)
            {
                s += String.Format("|{0,22}", o.ToString());
            }
            Log(s + "|");
        }
    }
}
