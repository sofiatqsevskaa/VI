from constraint import *

def sostanok(simona,marija, petar, sostanok):
    marija_termini = [14, 15, 18]
    simona_termini = [14, 19, 16, 13]
    petar_termini = [12, 13, 16, 17, 18, 19]
    if sostanok not in simona_termini or simona == 0:
        return False
    if sostanok not in marija_termini and marija == 1:
        return False
    if sostanok not in petar_termini and petar == 1:
        return False
    return petar + marija >= 1 and simona == 1


if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    prisustvo_domen = [0, 1]
    problem.addVariable("Simona_prisustvo", prisustvo_domen)
    problem.addVariable("Marija_prisustvo", prisustvo_domen)
    problem.addVariable("Petar_prisustvo", prisustvo_domen)
    # ----------------------------------------------------
    problem.addVariable("sostanok", [12, 13, 14, 15, 16, 17, 18, 19])
    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(sostanok,
                          ("Simona_prisustvo","Marija_prisustvo","Petar_prisustvo", "sostanok"))

    # ----------------------------------------------------

    for solution in problem.getSolutions():
        correct_solution = {'Simona_prisustvo': solution['Simona_prisustvo'],
                              'Marija_prisustvo': solution['Marija_prisustvo'],
                              'Petar_prisustvo': solution['Petar_prisustvo'],
                              'vreme_sostanok': solution['sostanok']}
        print(correct_solution)
