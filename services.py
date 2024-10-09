import os
from work_instruction import Work_Instruction
import openpyxl as xl

def createPartDir(part_number: str, root_path = "C:/Users/coole/OneDrive/Documents/Gestamp_Software_Projects/"):
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
