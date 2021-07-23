from QueueModule import Queue
from BigNumber import BigNumber
lst_q = []
##------------------------- Queue -------------------------#
q1 = Queue()
q1.enqueue('Assaf')
q1.enqueue('Nir')
q1.enqueue('Eliran')
q1.enqueue('Sagy')
test = 1
lst_q.append((test,q1.front() == 'Assaf'))
test = 2
lst_q.append((test,q1.rear() == 'Sagy'))
test = 3
lst_q.append((test,q1.dequeue() == 'Assaf'))
test = 4
lst_q.append((test,q1.queue == ['Nir', 'Eliran', 'Sagy']))
test = 5
lst_q.append((test,not q1.is_empty()))
test = 6
lst_q.append((test,len(q1) == 3))
test = 7
lst_q.append((test,q1.dequeue() == 'Nir'))
test = 8
lst_q.append((test,q1.dequeue() == 'Eliran'))
test = 9
lst_q.append((test,q1.dequeue() == 'Sagy'))
test = 10
try: 
    q1.dequeue()
except IndexError as err:
    lst_q.append((test,str(err) == 'The queue is empty'))
    
print(lst_q)

##------------------------- BigNumber -------------------------#
lst_bn = []

bn = BigNumber("123456789")

test = 1
lst_bn.append((test, str(bn) == '123456789'))
test = 2
try: 
    bn = BigNumber(55)
except TypeError as err:
    lst_bn.append((test,str(err) == 'BigNumber init expected str'))

test = 3
try: 
    bn = BigNumber('1234f56')
except TypeError as err:
    lst_bn.append((test,str(err) == 'The number contains non digit characters'))

test = 4
try: 
    bn == 2555
except TypeError as err:
    lst_bn.append((test,str(err) == 'Can only compare two BigNumbers'))

test = 5
bn2 = BigNumber('123456789')
lst_bn.append((test,bn == bn2))

test = 6
bn2 = BigNumber('123556789')
lst_bn.append((test,not bn == bn2))

test = 7
bn2 = BigNumber('123456789')
lst_bn.append((test,not bn > bn2))

test = 8
bn2 = BigNumber('12345678')
lst_bn.append((test,bn > bn2))

test = 9
bn2 = BigNumber('523456789')
lst_bn.append((test, not bn > bn2))

test = 10
bn2 = BigNumber('123456799')
lst_bn.append((test, not bn > bn2))

file_txt =  '8243975823649834734896\n'+\
            '1908365081756081734560187345601386457016837257801325\n' +\
            '953226532364148235412215158123125640134201520205130251021\n' +\
            '238745698236597283569827345697283569278345978234657829366\n' +\
            '941809932857103489516780345617803569813461597346578913569\n' +\
            '953226532364148235412215158123125640134201520205130251020\n' +\
            '183756713687817561575613459718356978146578913465\n' +\
            '1435619836581736598713654\n' +\
            '19873456971834657891364578913648756198346578193478561896'
## =============================================================================
## --------------------------------HERE-----------------------------------------
## =============================================================================
path = 'num_text.txt' # put here the path to the file
## =============================================================================
## This line will delete every change in the file
## =============================================================================

file = open(path, 'w')
file.write(file_txt)
file.close()

test = 11
lst_bn.append((test, bn.read_and_return_biggest(path) == BigNumber('953226532364148235412215158123125640134201520205130251021')))

test = 12
lst_bn.append((test, bn.read_and_return_biggest('') == None))

test = 13
bn.add_number_to_file(path)
file = open(path, 'r')
lst_bn.append((test, file.read() == file_txt + '\n' + str(bn)))
file.close()

test = 14
bn2 = BigNumber('937456938174569134651983649156398475619345')
bn2.add_number_to_file(path)
file = open(path, 'r')
lst_bn.append((test, file.read() == file_txt + '\n' + str(bn) + '\n' + str(bn2)))
file.close()

print(lst_bn)



#f=open('num_text.txt', 'r')
#read_f=f.read()
#print(f)
#print(read_f)
#f.close()
#list1=[]
#list1.append(read_f.read())
#print(list1[0])