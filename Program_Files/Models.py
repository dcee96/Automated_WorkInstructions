import json

class _HoleChecks:
    """ This class represents one hole on a part \n
        class variables:
            holes: list[str]
            nom_values: list[str]
            tolerances: list[str]
            description: list[str]
    """
    def __init__(self, **kwargs: list) -> None:
        self.hole_column = "I"
        self.nom_column = "J"
        self.tolerance_column = "K"
        self.description_column = "L"
        self.holes = kwargs.get("holes") if kwargs.get("holes") != None else []
        self.nom_values = kwargs.get("nom_values") if kwargs.get("nom_values") != None else []
        self.tolerances = kwargs.get("tolerances") if kwargs.get("tolerances") != None else []
        self.description = kwargs.get("description") if kwargs.get("description") != None else []

    def add_HoleCheck(self, **kwargs: list):
        self.holes.extend(kwargs.get("holes")) if kwargs.get("holes") != None else self.holes
        self.nom_values.extend(kwargs.get("nom_values")) if kwargs.get("nom_values") != None else self.nom_values
        self.tolerances.extend(kwargs.get("tolerances")) if kwargs.get("tolerances") != None else self.tolerances
        self.description.extend(kwargs.get("description")) if kwargs.get("description") != None else self.description

class _SpcPoints:
    """
        class variables:
            min_values: [float],
            max_values: [float],
            specs: [float]
    """
    def __init__(self, **kwargs: list[float]) -> None:
        self.specs = kwargs.get("specs") if kwargs.get("specs") != None else []
        self.min_values = kwargs.get("min_values") if kwargs.get("min_values") != None else []
        self.max_values = kwargs.get("max_values") if kwargs.get("max_values") != None else []

    def add_SpcPoints(self, **kwargs: list[float]) -> None:
        self.min_values.extend(kwargs.get("min_values")) if kwargs.get("min_values") != None else self.min_values
        self.max_values.extend(kwargs.get("max_values")) if kwargs.get("max_values") != None else self.max_values
    
    def getAll(self) -> tuple[list[float],list[float],list[float]]:
        return self.specs, self.min_values, self.max_values

class _ProfileChecks:
    """
        class variables:
            feeler: [str]
            max_tol: [float]
            min_tol: [float]
    """
    def __init__(self, **kwargs) -> None:
        self.feeler = kwargs.get("feeler") if kwargs.get("feeler") != None else []
        self.max_tol = kwargs.get("max_tol") if kwargs.get("max_tol") != None else []
        self.min_tol = kwargs.get("min_tol") if kwargs.get("min_tol") != None else []

class _TrimChecks:
    """
        class Variables:
            section: [str]
            max_tol: [float]
            min_tol: [float]
    """
    def __init__(self, **kwargs) -> None:
        self.section = kwargs.get("section") if kwargs.get("section") != None else []
        self.max_tol = kwargs.get("max_tol") if kwargs.get("max_tol") != None else []
        self.min_tol = kwargs.get("min_tol") if kwargs.get("min_tol") != None else []

class _TemplateChecks:
    """
        section: [str]
    """
    def __init__(self, **kwargs) -> None:
        self.section = kwargs.get("section") if kwargs.get("section") != None else []

class _VisualInspections:
    """
        section: [str]
    """
    def __init__(self, **kwargs) -> None:
        self.section = kwargs.get("section") if kwargs.get("section") != None else []

class WorkInstruction:

    """TODO: Redesign init to take in a dict that contains all relavent values needed
    to create a class. This dict should be created from the JSON module."""
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
                 visualInspection = _VisualInspections) -> None:
        
        self.partName = ("", partName)
        self.partNumber = ("", partNumber)
        self.sapNumber = ("", sapNumber)
        self.ecLevel = ("", ecLevel)
        self.department = (("L21", f"{department}  OPERATION PROCEDURE  AV GUAGE & FIXTURE: # 36447"),
                            ("I28", f"{department} OPERATION PROCEDURE"))
        self.holeChecks = holeChecks
        self.spcChecks = spcChecks
        self.profileChecks = profileChecks
        self.trimChecks = trimChecks
        self.templateChecks = templateChecks
        self.VisualInspection = visualInspection
    
    """TODO: Create a function that returns that work instruction in the form of a JSON str."""

    def to_json(self) -> json:
        return json