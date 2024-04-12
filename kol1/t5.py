from constraint import *



def ml(*args):
    for arg1 in args:
        for arg2 in args:
            if arg1 == arg2:
                continue
            if arg1.split("_")[1] == arg2.split("_")[1]:
                return False
    return True


def different_time_constraint(arg1, arg2):
    if arg1.split("_")[0] == arg2.split("_")[0] \
            and abs(int(arg1.split("_")[1]) - int(arg2.split("_")[1])) <= 1:
        return False
    return True

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = input()
    casovi_ML = input()
    casovi_R = input()
    casovi_BI = input()

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    AI_predavanja=[f"AI_cas_{i+1}" for i in range(int(casovi_AI))]
    ML_predavanja=[f"ML_cas_{i+1}" for i in range(int(casovi_ML))]
    R_predavanja=[f"R_cas_{i+1}" for i in range(int(casovi_R))]
    BI_predavanja=[f"BI_cas_{i+1}" for i in range(int(casovi_BI))]

    variables=["AI_vezbi","ML_vezbi","BI_vezbi"]
    variables.extend(AI_predavanja)
    variables.extend(ML_predavanja)
    variables.extend(R_predavanja)
    variables.extend(BI_predavanja)

    # ---Tuka dodadete gi ogranichuvanjata----------------

    problem.addVariables(AI_predavanja, AI_predavanja_domain)
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariables(ML_predavanja, ML_predavanja_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addVariables(R_predavanja, R_predavanja_domain)
    problem.addVariables(BI_predavanja, BI_predavanja_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)

    for var1 in variables:
        for var2 in variables:
            if var1 == var2:
                continue
            problem.addConstraint(different_time_constraint, (var1, var2))

    problem.addConstraint(ml, ML_predavanja + ["ML_vezbi"])

    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)