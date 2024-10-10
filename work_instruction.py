"""A class that can be used to represent a Work Instruction."""

class Work_Instruction:

    """
    It should be noted that if the part gets cut into two
    in the laser deptartment then that should be reflected
    in the part numbers.

    example:
        The Stamping 3QF.804.119-120 will become 3QF.804.120 and 3QF.804.119 after it is laser cut.
    """

    def __init__(self, part_num, ec_lvl, part_name, sap_num, instructions: dict, dept: str):
        #J34
        self.part_number = ("J34", part_num)
        #M34
        self.ec_level = ("M34", ec_lvl)
        #J35
        self.sap_number = ("J35", sap_num)
        #J32
        self.part_name = ("J32", part_name)

        self.instructions = instructions

        self.dept = dept
    
    def toString(self):
        workInstructionString = f"""
        Part name: {self.part_name[1]},
        Part number: {self.part_number[1]},
        SAP number: {self.sap_number[1]},
        EC Level: {self.ec_level[1]}
        """

        return workInstructionString
