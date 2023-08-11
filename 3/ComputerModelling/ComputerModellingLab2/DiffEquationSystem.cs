using System;
using System.Collections.Generic;

namespace ComputerModellingLab2
{
    public class DiffEquationSystem
    {
        private List<Func<Dot, double, double>> equations;

        public DiffEquationSystem(List<Func<Dot, double, double>> equations){
            this.equations = equations;
        }
        public DiffEquationSystem(params Func<Dot, double, double>[] funcs){
            this.equations = new List<Func<Dot, double, double>>();
            foreach(var i in funcs){
                this.equations.Add(i);
            }
        }
        public Func<Dot, double, double> this[int n] => equations[n];
        public List<double> Substitute(Dot dot, double t){
            var ret = new List<double>();
            foreach(var func in equations){
                ret.Add(func(dot, t));
            }
            return ret;
        }
    }
}