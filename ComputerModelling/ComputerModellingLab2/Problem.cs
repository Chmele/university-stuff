namespace ComputerModellingLab2
{
    public class Problem
    {
        private DiffEquationSystem system;
        private Dot start;

        public Problem(DiffEquationSystem system, Dot start){
            this.system = system;
            this.start = start;
        }
        public Dot Start{get => this.start;}

        public Dot EvalInDot(Dot prev, double t){
            return new Dot(system.Substitute(prev,t));
        }
    }
}