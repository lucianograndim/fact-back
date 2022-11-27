from fpdf import FPDF

class PDF(FPDF):

    def lines(self):
        self.set_fill_color(155.0, 155, 155.0)
        self.rect(5.0, 5.0, 205.9,270.4,'DF')
        self.set_fill_color(255, 255, 255) 
        self.rect(8.0, 8.0, 199.9,265.4,'FD')
    def imagex(self):
        self.set_xy(10.0,9.0)
        self.image('alloxentric_logo-3x.png',  link='', type='', w=1580/40, h=1000/80)

    def titles(self):
        self.set_xy(0.0,0.0)
        self.set_font('Times', 'B', 25)
        self.set_text_color(0, 0, 0)
        self.cell(w=220.0, h=40.0, align='C', txt="FACTURA POR SERVICIOS", border=0)

pdf = PDF(orientation='P', unit='mm', format='Letter')
pdf.add_page()
pdf.lines()
pdf.imagex()
pdf.titles()
pdf.output('test.pdf','F')