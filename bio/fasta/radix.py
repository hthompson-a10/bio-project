class RadixSort(object):

    def _counting_sort(self, input_list, place, radix=10):
        size = len(input_list)
        counts = [0] * radix
        output_list = [0] * size

        for i in range(0, size):
            idx = (input_list[i].cnt // place) % radix
            counts[idx] += 1

        for i in range(1, radix):
            counts[i] += counts[i - 1]

        i = size - 1
        while i >= 0:
            idx = (input_list[i].cnt // place) % radix
            output_list[counts[idx] - 1] = input_list[i]
            counts[idx] -= 1
            i -= 1

        for i in range(0, size):
            input_list[i] = output_list[i]

    def sort(self, input_list, max_val):
        place = 1
        while max_val // place > 0:
            self._counting_sort(input_list, place)
            place *= 10
