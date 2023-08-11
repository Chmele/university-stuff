using System;
using System.Collections.Generic;
using System.Text;

namespace ChMLab1.Interfaces
{
    interface ILogger
    {
        public void Log(string s);
        public void Log(params object[] list);
        public void Log(List<double> l);
    }
}
