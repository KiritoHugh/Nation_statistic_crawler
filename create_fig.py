import numpy as np
import matplotlib.pyplot as plt

def drawHW1(result):
    result = np.array(result)
    year = result[:,0]
    total = result[:,1]
    man = result[:,2]
    woman = result[:,3]
    city = result[:,4]
    cotrysd = result[:,5]

    fig = plt.figure(figsize = (15,5))
    # plt.bar(year,total,tick_label = year.astype('int').tolist(),width = 0.6)
    plt.bar(year,man,tick_label = year.astype('int').tolist(),width = 0.6,label = 'man')
    plt.bar(year,woman,tick_label = year.astype('int').tolist(),width = 0.6,bottom=man,label = 'woman')
    plt.xlabel('Year')
    plt.ylabel('Population/*10^4')
    plt.title('Total')
    plt.legend(loc='lower left')
    plt.grid()
    plt.savefig('HW1_1.png')
    plt.show()

    fig = plt.figure(figsize = (15,5))
    # plt.bar(year,total,tick_label = year.astype('int').tolist(),width = 0.6)
    plt.bar(year,city,tick_label = year.astype('int').tolist(),width = 0.6,label = 'city')
    plt.bar(year,cotrysd,tick_label = year.astype('int').tolist(),width = 0.6,bottom=city,label = 'countryside')
    plt.xlabel('Year')
    plt.ylabel('Population/*10^4')
    plt.title('Total')
    plt.legend(loc='lower left')
    plt.grid()
    plt.savefig('HW1_2.png')
    plt.show()


    man_ratio = man/total
    city_ratio = city/total

    fig = plt.figure(figsize = (15,5))
    plt.plot(year,man_ratio,'^-',label = 'man')
    plt.plot(year,1-man_ratio,'o-',label = 'woman')
    plt.xticks(year.astype('int').tolist())
    plt.xlabel('Year')
    plt.ylabel('Population proportion')
    plt.title('Man vs Woman')
    plt.legend()
    plt.grid()
    plt.savefig('HW1_3.png')
    plt.show()


    fig = plt.figure(figsize = (15,5))
    plt.plot(year,city_ratio,'^-',label = 'city')
    plt.plot(year,1-city_ratio,'o-',label = 'countryside')
    plt.xticks(year.astype('int').tolist())
    plt.xlabel('Year')
    plt.ylabel('Population proportion')
    plt.title('City vs Countryside')
    plt.legend()
    plt.grid()
    plt.savefig('HW1_4.png')
    plt.show()


def drawHW2(d,result):
    result = np.array(result)
    # print(result)
    for i in range(len(d)):
        cmd = 'result[:,{}]'.format(str(i))
        locals()[d[i]] = eval(cmd)
        # print(cmd)
        # print(locals()['year'])
    # print(locals())

    fig = plt.figure(figsize = (15,5))
    plt.plot(locals()['year'],locals()['born'],'^-',label = 'Born')
    plt.plot(locals()['year'],locals()['die'],'o-',label = 'Die')
    plt.plot(locals()['year'],locals()['increase'],'*-',label = 'Increase')
    plt.xticks(locals()['year'].astype('int').tolist())
    plt.xlabel('Year')
    plt.ylabel('Ratio/%')
    plt.title('Population change ratio')
    plt.legend()
    plt.grid()
    plt.savefig('HW2_ratio.png')
    plt.show()

    c1998 = 100
    popu = (1+locals()['increase']/100)
    inc = np.multiply.accumulate(popu[::-1])[::-1]
    popu = c1998*inc
    fig = plt.figure(figsize = (15,5))
    # plt.bar(year,total,tick_label = year.astype('int').tolist(),width = 0.6)
    plt.bar(locals()['year'],popu,tick_label = locals()['year'].astype('int').tolist(),width = 0.6,label = 'population')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population (assume 1998 is 100)')
    plt.legend(loc='lower left')
    plt.grid()
    plt.savefig('HW2_popu.png')
    plt.show()


