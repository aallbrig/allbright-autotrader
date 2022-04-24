from model.reports.StockDaySummary import StockDaySummary
from model.reports.StockNowSummary import StockNowSummary


class Stock:
    _symbol: str = None
    _now_summary: StockNowSummary = None
    _day_summaries: list[StockDaySummary] = None

    def __init__(self, symbol: str):
        self._symbol = symbol

    def symbol(self) -> str:
        return self._symbol

    def set_day_summary(self, summary: StockNowSummary):
        self._now_summary = summary

    def now_summary(self) -> StockNowSummary:
        return self._now_summary

    def __str__(self):
        return self._console_view()

    def _console_view(self):
        maybe_summary = f' {self._now_summary}' if self._now_summary is not None else ''
        return f'Stock: {self.symbol()}{maybe_summary}'

    def set_historic_data(self, historic_day_summaries: list[StockDaySummary]):
        self._day_summaries = historic_day_summaries
