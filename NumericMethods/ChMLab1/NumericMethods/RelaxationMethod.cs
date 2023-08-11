using System;
using System.Collections.Generic;
using System.Text;
using ChMLab1.Interfaces;

namespace ChMLab1
{
    class RelaxationMethod : NumericMethod
    {
        private double tau = -0.0434;
        public RelaxationMethod(double precision) : base(precision) { }
        public RelaxationMethod(double precision, ILogger l) : base(precision, l) { }

        public override double Iterate(double x, Polynom p)
        {
            return x + tau * p.Value(x);
        }
    }
}
