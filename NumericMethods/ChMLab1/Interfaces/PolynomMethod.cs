using System;

namespace ChMLab1.Interfaces
{
    abstract class NumericMethod
    {
        protected double precision;
        public ILogger logger;

        public NumericMethod(double precision)
        {
            this.precision = precision;
            logger = new NullLogger();
        }

        public NumericMethod(double precision, ILogger logger)
        {
            this.precision = precision;
            this.logger = logger;
        }

        public double Seek(double x, Polynom p)
        {
            while (!Stop(x, p))
            {
                logger.Log(x,p.Value(x));
                x = Iterate(x, p);
            }
            logger.Log(x, p.Value(x));
            return x;
        }

        protected bool Stop(double x, Polynom p)
        {
            double x2 = Iterate(x, p);
            return precision > Math.Abs(x2 - x) ||
                   precision > Math.Abs(p.Value(x2) - p.Value(x));
        }

        protected bool Stop(double x, double x2, Polynom p)
        {
            return precision > Math.Abs(x2 - x) ||
                   precision > Math.Abs(p.Value(x2) - p.Value(x));
        }

        abstract public double Iterate(double x, Polynom p);
    }
}
