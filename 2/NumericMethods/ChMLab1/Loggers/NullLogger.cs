using System;
using System.Collections.Generic;
using System.Text;
using ChMLab1.Interfaces;

namespace ChMLab1
{
    class NullLogger :ILogger 
    {
        public NullLogger() { }
        public void Log(string s)
        {
            return;
        }

        public void Log(params object[] list)
        {
            return;
        }

        public void Log(List<double> l)
        {
            throw new NotImplementedException();
        }
    }
}
