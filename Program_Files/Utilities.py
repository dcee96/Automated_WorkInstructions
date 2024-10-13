import qrcode
import os
import openpyxl
import WorkInstruction

class Utilites:
    def __init__(self) -> None:
        pass

    def generate_QRCode(self, link: str, fileName: str, fileDestination: str) -> None:
        """
            Arguments: 
                link: a string of a url that points to the PDF.
                fileName: a string of the name that will be given to the png file
                    that contains the QR Code.
                fileDestination: a string of the directory the png file will be saved to.
            
            Returns: None    
        """
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L)

        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        img.save(os.path.join(fileDestination, f"{fileName}.png")) 

    def create_WorkInstruction(self, workInstruction: WorkInstruction, fileDestination: str) -> None:
        wb = openpyxl.load_workbook("Automated_WorkInstructions\Assets\CheckingFixtureInstructionTemplate.xlsx")
        workSheets = wb.sheetnames