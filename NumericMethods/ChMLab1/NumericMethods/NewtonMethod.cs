using ChMLab1.Interfaces;
using System;

namespace ChMLab1
{
    class NewtonMethod : NumericMethod
    {
        public NewtonMethod(double precision) : base(precision) { }
        public NewtonMethod(double precision, ILogger l) : base(precision,l) { }

        public override double Iterate(double x, Polynom p)
        {
            return x - p.Value(x) / p.Derivative().Value(x);
        }
    }
}
