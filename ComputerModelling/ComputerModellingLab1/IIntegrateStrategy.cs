namespace ComputerModelling
{
    public interface IIntegrateStrategy
    {
        public double GetRungeTheta();
        public double Integrate(Problem p);
    }
}