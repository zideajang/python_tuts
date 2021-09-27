# 程序员绕不开的算法6 —快速排序算法 lomuto 和 hoare 划分
# 
class Sort:
    def _quicksort(self, array: list, low: int, high: int):
        if low < high:
            pivot = self.hoare_partition(array, low, high)
            self._quicksort(array, low, pivot)
            self._quicksort(array, pivot + 1, high)

    def hoare_partition(self, array: list, low: int, high: int) -> int:
        pivot = array[(high + low) // 2]
        # pivot = array[low]
        i = low
        j = high

        while True:
            
            while array[i] < pivot:
                i += 1

            while array[j] > pivot:
                j -= 1

            if i >= j:
                return j
            
            array[i], array[j] = array[j], array[i]

    def sort(self, array: list) -> list:
        self._quicksort(array, 0, len(array) - 1)
        return array

if __name__ == "__main__":
    arr = [11,9,29,7,2,15,28]
    sort = Sort()
    print(sort.sort(arr))
