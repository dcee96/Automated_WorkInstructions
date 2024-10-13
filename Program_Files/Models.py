class __Hole:
    """ This class represents one hole on a part """
    def __init__(self,
                hole,
                nom_size,
                tol, 
                desc ) -> None:
        
        self.hole = ("",hole),
        self.nominal_size = ("", nom_size),
        self.tolerance = ("", tol),
        self.description = ("", desc)

class __Spc:
    def __init__(self,
                 min_value,
                 max_value ) -> None:
        
        self.min_value = min_value
        self.max_value = max_value

class __Profile:
    def __init__(self) -> None:
        pass

class __Trim:
    def __init__(self) -> None:
        pass

class __TemplateCheck:
    def __init__(self) -> None:
        pass

class __VisualInspection:
    def __init__(self) -> None:
        pass

class WorkInstruction:
    def __init__(self,
                 partName,
                 partNumber,
                 sapNumber,
                 ecLevel,
                 holeChecks: list[__Hole],
                 spcChecks: list[__Spc],
                 profileChecks: list[__Profile],
                 trimChecks: list[__Trim],
                 templateChecks: list[__TemplateCheck],
                 VisualInspection: list[__VisualInspection] ) -> None:
        
        self.partName = partName