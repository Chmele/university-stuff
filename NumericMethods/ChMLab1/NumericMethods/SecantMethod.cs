using ChMLab1.Interfaces;
using System;

namespace ChMLab1
{
    class SecantMethod : NumericMethod
    {
        public SecantMethod(double precision) : base(precision) { }
        public SecantMethod(double precision, ILogger l) : base(precision, l) { }

        public override double Iterate(double x, Polynom p){ return 0; }

        new public double Seek(double x, Polynom p)
        {
            double x2 = p.Value(x) / p.Derivative().Value(x);
            while (!Stop(x, x2, p))
            {
                logger.Log(x, x2, p.Value(x));
                var buffer = x;
                x -= (x - x2) * p.Value(x) / (p.Value(x) - p.Value(x2));
                x2 = buffer;
            }
            return x;
        }
    }
}

