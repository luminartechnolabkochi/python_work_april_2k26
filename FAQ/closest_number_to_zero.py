

class ClosestToZero:


    def solution(self,arr):

        closest = arr[0]

        for num in arr:

            if abs(num) < abs(closest):

                closest = num

        if closest < 0 and abs(closest) in arr:

            print(abs(closest))

        else:

            print(closest)

cls =  ClosestToZero()

cls.solution([-1,2,4])

