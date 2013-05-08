'''
Created on 24 Apr 2013

@author: jrem
'''
from org.muscat.staldates.aldatesx.ui.tests.GuiTest import GuiTest
from org.muscat.staldates.aldatesx.ui.widgets.OutputsGrid import OutputsGrid


class TestOutputsGrid(GuiTest):

    def setUp(self):
        GuiTest.setUp(self)

    def testDisplayInputNames(self):
        og = OutputsGrid()
        self.assertEqual("-", self.findButton(og, "Projectors").inputDisplay.text())

        og.updateOutputMappings({2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 0})
        self.assertEqual("Camera 1", self.findButton(og, "Projectors").inputDisplay.text())
        self.assertEqual("Camera 2", self.findButton(og, "Font").inputDisplay.text())
        self.assertEqual("Camera 3", self.findButton(og, "Church").inputDisplay.text())
        self.assertEqual("DVD", self.findButton(og, "Welcome").inputDisplay.text())
        self.assertEqual("Extras", self.findButton(og, "Gallery").inputDisplay.text())
        self.assertEqual("Visuals PC", self.findButton(og, "Special").inputDisplay.text())
        self.assertEqual("Blank", self.findButton(og, "Record").inputDisplay.text())