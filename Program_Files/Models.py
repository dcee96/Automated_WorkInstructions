class _HoleChecks:
    """ This class represents one hole on a part \n
        class variables:
            holes: list[str]
            nom_values: list[str]
            tolerances: list[str]
            description: list[str]
    """
    def __init__(self, **kwargs: list) -> None:
        self.values = kwargs

class _SpcPoints:
    """ There should be two keys, lcl and ucl. Each key should have a list of floats 
    associated to it. The index of the list values +1 should be used to indicate the
    spc number. """
    def __init__(self, **kwargs: list[float]) -> None:
        self.values = kwargs

class _ProfileChecks:
    """ There should be three keys, feelers, ucl and lcl. Each key should have a list of values 
    associated with it. The index of the list values +1 should be used to indicate the
    profile check number. """
    def __init__(self, **kwargs) -> None:
        self.values = kwargs

class _TrimChecks:
    """ There should be two keys, lcl and ucl. Each key should have a list of floats 
    associated to it. The index of the list values +1 should be used to indicate the
    trim check number. """
    def __init__(self, **kwargs) -> None:
        self.values = kwargs

class _TemplateChecks:
    """ This will just be a list of different template checks that may be used."""
    def __init__(self, *args) -> None:
        self.values = args

class _VisualInspections:
    """ This will just be a list of different Visual defects that should be monitored."""
    def __init__(self, *args) -> None:
        self.values = args

class WorkInstruction:
    def __init__(self,
                 partName: str,
                 partNumber: str,
                 sapNumber: str,
                 ecLevel: str,
                 department: str,
                 holeChecks = _HoleChecks,
                 spcChecks = _SpcPoints,
                 profileChecks = _ProfileChecks,
                 trimChecks = _TrimChecks,
                 templateChecks = _TemplateChecks,
                 visualInspection = _VisualInspections ) -> None:
        
        self.partName = ("J32", partName)
        self.partNumber = ("J34", partNumber)
        self.sapNumber = ("J35", sapNumber)
        self.ecLevel = ("", ecLevel)
        self.department = (["L21", f"{department} OPERATION PROCEDURE  AV GUAGE & FIXTURE: # 36447"], ["I28", f"{department} OPERATION PROCEDURE"])
        self.holeChecks = ("Hole Checks","I2:M20", holeChecks.values)
        self.spcChecks = ("SPC Checks","I2:M20", spcChecks.values)
        self.profileChecks = ("Profile Checks","I2:M20", profileChecks.values)
        self.trimChecks = ("Trim Checks","I2:M20", trimChecks.values)
        self.templateChecks = ("Template checks","I2:M20", templateChecks.values)
        self.VisualInspection = ("Visual inspection","I2:M20", visualInspection.values)
