# import the data
import urllib2
url = "http://spark-public.s3.amazonaws.com/algo1/programming_prob/QuickSort.txt"
file = urllib2.urlopen(url)
data = []
for line in file: 
    data.append(int(line))

class Solution():
    data = []
    def iteSort(self, idx0, idx1):
        pivot = self.data[idx0]
        i = idx0 + 1
        for j in range(idx0 + 1, idx1):
            if self.data[j] < pivot:
                tmp = self.data[j]
                self.data[j] = self.data[i]
                self.data[i] = tmp
                i += 1
        if (i - 1) != idx0:
            self.data[idx0] = self.data[i - 1]
            self.data[i - 1] = pivot
        if (i > idx0 + 1):
            count1 = self.iteSort(idx0, i)
        else:
            count1 = 0
        if (idx1 - i > 2):
            count2 = self.iteSort(i + 1, idx1)
        else:
            count2 = 0
        return count1 + count2 + (idx1 - idx0 - 1)
        
    def quickSort(self, data):
        self.data = data
        count = self.iteSort(0, len(data))
        return [self.data, count]
        
sol = Solution()
[data, count] = sol.quickSort(data)
print len(data)
print count
