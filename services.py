import os
from work_instruction import Work_Instruction
from openpyxl.utils import get_column_letter as column_letter
import openpyxl as xl

def createPartDir(part_number: str, root_path = "/Users/dylancooley/Documents/Automated_WI"):
    try:
        os.mkdir(f"{root_path}/{part_number}")
    except:
        print(f"Directory {part_number} already exists.")

    return root_path + part_number

def createWiWorkbook(work_instr: Work_Instruction, dest: str):
    wb = xl.load_workbook(r"Automated_WorkInstructions\Assets\CheckingFixtureInstructionTemplate.xlsx")
    ws = wb["OP"]

    ws[work_instr.ec_level[0]].value = work_instr.ec_level[1]
    ws[work_instr.part_number[0]].value = work_instr.part_number[1]
    ws[work_instr.sap_number[0]].value = work_instr.sap_number[1]
    ws[work_instr.part_name[0]].value = work_instr.part_name[1]

    try:
        wb.save(f"{dest}/{work_instr.part_number[1]}.xlsx")
    except(Exception):
        print(EncodingWarning)
    wb.close()

def pullOldData(file_path):
    """
    TODO:
        This function should loop through A1:H36 and I20:M20 
        storing all of the cell values as it goes. This should then
        be repeated for all sheets.

        The return value will be the collection of all of the data of 
        that workbook.
    """
    wb = xl.load_workbook(file_path)
    sheets = wb.sheetnames

    oldData = {}

    for sheet in sheets:
        data_list = []
        if (sheet != "data"):
            ws = wb[sheet]
            for col in range(1, 9):
                letter = column_letter(col)
                for row in range(1,37):
                    data_list.append((f"{letter}{row}", ws[f"{letter}{row}"].value))
        oldData[str(sheet)] = data_list

    return oldData

def storeOldData(old_data):
    """
    TODO:
        This function should use the collection of old data to upload it to
        the newly created workbook.
    """

def getAllFilePaths(parent_folder_path):
    
    file_paths = {}

    for root_path, sub_dir, files in os.walk(parent_folder_path):
        if (root_path != '/Volumes/DBCdisk/Gestamp/Updated_Work_Instructions'):
            folders = root_path.split('/')
            file_paths[str(folders[-1])] = {str(root_path): files}
    
    return file_paths

allOldData = getAllFilePaths("/Volumes/DBCdisk/Gestamp/Updated_Work_Instructions/")
#print(allOldData.get("3QF_801_253")[list(allOldData.get("3QF_801_253"))[0]][0])
print(pullOldData(f"{list(allOldData.get("3QF_801_253"))[0]}/{allOldData.get("3QF_801_253")[list(allOldData.get("3QF_801_253"))[0]][0]}"))