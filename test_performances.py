import time
import matplotlib.pyplot as plt

def plot_results(list_of_numbers,labels = ['Class','No_Class']):
    
    plt.bar(labels,list_of_numbers)
    plt.ylabel("seconds")
    plt.savefig('./results_code_efficiency.png')
    

def testing_time_classes():
    results = 0
    print("Testing class methods")
    for n in range(1000):
        start_time = time.time()
        from get_associations_class import epidemiology
        associationsretriever = epidemiology()
#        associationsretriever.get_associations()
        end_time = time.time()
        execution_time = end_time - start_time
        results += float(execution_time)
    return results
    
def testing_time():
    
    results = 0
    print("Testing no class method")
    for n in range(1000):
        start_time = time.time()
        from get_associations import get_associations
        end_time = time.time()
#       get_associations
        execution_time = end_time - start_time
        results += float(execution_time)
    print(results)
    return results


def Main():
    resu = []
    test_classes = testing_time_classes()
    resu.append(test_classes)
    test_no_classes = testing_time()
    resu.append(test_no_classes)
    plot_results(resu)


if __name__ == '__main__':
    Main()