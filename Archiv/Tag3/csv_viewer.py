import wx
import wx.grid
import pandas as pd

class App(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(800, 600))
        self.panel = wx.Panel(self)
        self.create_widgets()
        self.Centre()
        self.Show()

    def create_widgets(self):
        file_button = wx.Button(self.panel, label="Open file")
        file_button.Bind(wx.EVT_BUTTON, self.open_file)
        self.grid = wx.grid.Grid(self.panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(file_button, 0, wx.ALL|wx.EXPAND, 5)
        vbox.Add(self.grid, 1, wx.ALL|wx.EXPAND, 5)
        self.panel.SetSizer(vbox)

    def open_file(self, event):
        with wx.FileDialog(self, "Open Excel file", wildcard="Excel files (*.xlsx)|*.xlsx",
                           style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return
            # read excel file into pandas dataframe
            file_path = file_dialog.GetPath()
            df = pd.read_excel(file_path)
            # set grid rows and columns
            self.grid.CreateGrid(df.shape[0], df.shape[1])
            for i, col in enumerate(df.columns):
                self.grid.SetColLabelValue(i, str(col))
            # set grid cell values
            for i, row in df.iterrows():
                for j, val in enumerate(row):
                    self.grid.SetCellValue(i, j, str(val))

if __name__ == '__main__':
    app = wx.App()
    frame = App(None, title="Excel Viewer")
    app.MainLoop()
