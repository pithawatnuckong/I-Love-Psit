'''BusStop I'''
def main(capital, sign):
    '''calculator'''
    service, answer = [], 0
    for _ in range(sign):
        people = (input().strip()).split(" ")
        bus_stop = int(people.pop(0))
        while bus_stop in service:
            service.remove(bus_stop)
            answer += 1
        for check in people:
            if int(check) > bus_stop and len(service) < capital:
                service += [int(check)]
    print(answer)
main(int(input()), int(input()))
