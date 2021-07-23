
from Matrix import Matrix
from VectorModule import Vector

def main():
    results_file = "my_results3.txt"

    ################ checking the Vector vec field - content and type (2 tests) ################
    
    v1_stud = Vector([2, 4, 6, 8, 10])
    if type(v1_stud)!=Vector:
        raise "Bad Vector type"
    stud_vec_cont = v1_stud.vec
    with open(results_file, 'w') as f:
        f.write("v1_stud:\n")
        f.write("%s\n" % str(v1_stud))
        f.write("stud_vec_content:\n")
        f.write("%s\n" % str(stud_vec_cont))
        
    f.close()

    ###### checking immutability - if v1 changes after adding v2 ######

    v2_stud = Vector([1, 3, 5, 7, 9])
    # Checking if v1_stud will be changed
    v1_stud + v2_stud
    with open(results_file, 'a') as f:
        f.write("After adding [1,3,5,7,9]:\n")
        f.write("%s\n" % str(v1_stud))
    f.close()

    ###### Indexing - if works well and takes the proper element ######

    third_stud = v1_stud[3]
    with open(results_file, 'a') as f:
        f.write("v1_stud[3]=\n")
        f.write("%s\n" % str(third_stud))
    f.close()
    
    ###### Matrix - checking the shape - content and type (2 tests) ######

    m1_stud = Matrix([v1_stud, v2_stud])
    if type(m1_stud)!=Matrix:
        raise "Bad Matrix type"
    with open(results_file, 'a') as f:
        f.write("The matrix content:\n")
        f.write("%s\n" % str(m1_stud.content))
        f.write("The matrix shape:\n")
        f.write("%s\n" % str(m1_stud.shape))
    f.close()

    ###### Matrix - transpose - result and immutability ######
    m1_transposed_stud = m1_stud.transpose()
    with open(results_file, 'a') as f:
        f.write("The transposed matrix content:\n")
        f.write("%s\n" % str(m1_transposed_stud.content))
        f.write("The transposed matrix shape:\n")
        f.write("%s\n" % str(m1_transposed_stud.shape))
    f.close()


main()
