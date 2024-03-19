import tiny_solver
from tiny_solver import GaussNewtonOptimizer, Problem, LinearSolver, OptimizerOptions
from tiny_solver.factors import PriorFactor, BetweenFactorSE2
from tiny_solver.loss_functions import HuberLoss
import numpy as np


def main():
    print(f"{tiny_solver.__version__=}")
    print(dir(tiny_solver))

    print(dir(LinearSolver.SparseCholesky))
    opt_option = OptimizerOptions(linear_solver_type=LinearSolver.SparseQR, max_iteration=12, verbosity_level=1)
    print(opt_option)
    loss = HuberLoss(1.0)
    print(loss)
    exit()
    # print(tiny_solver.sum_as_string(1, 2))

    # tiny_solver.mult(np.zeros((1, 2)))
    # a = tiny_solver.Dual64()
    # print(a.first_derivative)
    b = BetweenFactorSE2(1.0, 2.0, 3.0)
    # print("factor module\n", dir(factors))
    # b = Costf(1.0, 2.0, 3.0)

    print(type(b))
    print(dir(b))
    print(b)
    problem = Problem()
    print(dir(problem))
    problem.num = 200
    print(problem.num)
    d = PriorFactor(np.array([1.0, 2.0, 3.0]))
    problem.add_residual_block(1, [("aa", 1)], d)
    problem.add_residual_block(1, [("aaa", 1)], b)
    # c.add_residual_block(1, [("aaa", 1)])
    # c.add_residual_block(1, [("aa", 1)])
    # d = tiny_solver.BetweenFactor()
    # d.ttt()
    # tiny_solver.te(d)
    optimizer = GaussNewtonOptimizer()
    # optimizer.optimize(problem, {"aa": np.array([123, 2, 3, 4], dtype=np.float64)})


if __name__ == "__main__":
    main()
