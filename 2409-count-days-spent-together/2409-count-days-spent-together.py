class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def date_to_day(date: str) -> int:
            month = int(date[:2])
            day = int(date[3:])
            return sum(days_in_month[:month - 1]) + day
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        if start > end:
            return 0
        return date_to_day(end) - date_to_day(start) + 1