# res = ""
#
# string = "minutes1.  Inclusion-exclusion principle and it’s derivation via expectations; probability of derangements2.  Conditional probability, total probability rule, multiplication rule; examples of application3.  Bayes formula; examples of application4.  Discrete random variables; their properties and generating functions5.  Continuous random variables; their properties and generating functions6.  Expected value; linearity; total probability rule for expectation of discrete and continuous variables.7.  Moments; variance; correlation.  Variance of linear combinations of random variables.  Covariance andindependence8.  Independent random variables; examples and properties9.  Normal distribution and its properties10.  Exponential  distribution  (scaling,  sums,  memorylessness  property,  relation  to  Gamma-distributionsand Poisson processes)11.  Joint and marginal distributions; conditional distribution12.  Law of large numbers; examples and applications13.  Central Limit theorem; examples and applications14.  Markov chains; states and limiting probability distribution, absorption probabilities15.  Poisson processes:  definition, examples and properties"
# for i in range(len(string)-1):
#     res += string[i]
#     if '0' <= string[i+1] <= '9' and (string[i] < '0' or string[i] > '9'):
#         res += "\n\n"
# print(res)
#
#
# import serial
#
# ser = serial.Serial(
#     port='COM3',
#     baudrate=9600)
#     # stopbits=serial.STOPBITS_ONE,
#     # bytesize=serial.EIGHTBITS,
#     # timeout=0)
#
#
# serialString = ""                           # Used to hold data coming over UART
#
#
# while(1):
#
#     # Wait until there is data waiting in the serial buffer
#     if(serialPort.in_waiting > 0):
#
#         # Read data out of the buffer until a carraige return / new line is found
#         serialString = serialPort.readline()
#
#         # Print the contents of the serial data
#         print(serialString.decode('Ascii'))
#
#         # Tell the device connected over the serial port that we recevied the data!
#         # The b at the beginning is used to indicate bytes!
#         serialPort.write(b"Thank you for sending data \r\n")



def find_rebra(T, v, w):
    visited = set()
    path = DFS_recursive(T, v, w, visited)


# A function to return a set of edges between v and w
def DFS_recursive(T, vertex, w, visited):
    visited.add(vertex)
    for neighbour in T.graph[vertex]:
        if neighbour not in visited:
            if neighbour == w:  # ми найшли шлях
                return [T.graph[vertex][w]]  # додаємо ребро (vertex, w) до списку
            result = DFS_recursive(neighbour, visited)
            if result:  # це буде тру тільки якщо ми дійдемо до вершини w
                # додаємо ребро (vertex, neighbour) до списку
                result.append(T.graph[vertex][neighbour])
                return result
    # if there are no neighbours:
    return False












