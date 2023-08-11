using System;

namespace ComputerModelling
{
    public class Problem : IIntegrable
    {
        public Func<double, double> Func { get => f; }
        public Range Range { get => range; }
        public double Eps { get => eps; }
        private Func<double, double> f { get; }
        private Range range { get; }
        private double eps;
        public Problem(Func<double, double> func, Range range, double eps)
        {
            this.f = func;
            this.range = range;
            this.eps = eps;
        }
        public double Integrate(IIntegrateStrategy s)
        {
            return s.Integrate(this);
        }
    }
}