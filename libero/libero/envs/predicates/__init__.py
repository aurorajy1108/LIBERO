from .base_predicates import *


VALIDATE_PREDICATE_FN_DICT = {
    "true": TruePredicateFn(),
    "false": FalsePredicateFn(),
    "not": Not(),
    "and": And(),
    "or": Or(),
    "any": Any(),
    "all": All(),
    "in": In(),
    "equal": Equal(),
    "minus": Minus(),
    "greaterthan": GreaterThan(),
    "lessthan": LessThan(),
    "distance": Distance(),
    "planardistance": PlanarDistance(),
    "incontact": InContact(),
    "on": On(),
    "relaxedon": RelaxedOn(),
    "up": Up(),
    "stackbowl": StackBowl(),
    "printjointstate": PrintJointState(),
    "open": Open(),
    "close": Close(),
    "openratio": OpenRatio(),
    "staircase": StairCase(),
    "inair": InAir(),
    "sameheight": SameHeight(),
    "turnon": TurnOn(),
    "turnoff": TurnOff(),
    "upsidedown": UpsideDown(),
    "upright": Upright(),
    "axisalignedwithin": AxisAlignedWithin(),
    "under": Under(),
    "posigreaterthan": PosiGreaterThan(),
    "posilessthan": PosiLessThan(),
    "positionwithin": PositionWithin(),
    "positionwithinobject": PositionWithinObject(),
    "positionwithinobjectannulus": PositionWithinObjectAnnulus(),
    "getposi": GetPosi(),
    "printgeomstate": PrintGeomState(),
    "above": Above(),
    "between": MidBetween(),
    "relaxedbetween": RelaxedMidBetween(),
    "linear": Linear(),
    "ordering": LROrdering(),
    "distancebetween": DistanceBetween(),
    "flexibleon": FlexibleOn(),
    "orientedatdegree": OrientedAtDegree(),
    "getorientation": GetOrientation(),
    "lrordering": LROrdering(),
    "posisamewith": PosiSameWith(),
    "orderalongaxis": OrderAlongAxis(),
    "midbetween": MidBetween(),
    "relaxedmidbetween": RelaxedMidBetween(),
    "axisalignedwithinworldaxis": AxisAlignedWithinWorldAxis(),
    "istouchingsideaxis": IsTouchingSideAxis(),
    "neuraljudge": NeuralJudge(),
}


def update_predicate_fn_dict(fn_key, fn_name):
    VALIDATE_PREDICATE_FN_DICT.update({fn_key: eval(fn_name)()})


def eval_predicate_fn(predicate_fn_name, *args):
    assert predicate_fn_name in VALIDATE_PREDICATE_FN_DICT
    return VALIDATE_PREDICATE_FN_DICT[predicate_fn_name](*args)


def get_predicate_fn_dict():
    return VALIDATE_PREDICATE_FN_DICT


def get_predicate_fn(predicate_fn_name):
    return VALIDATE_PREDICATE_FN_DICT[predicate_fn_name.lower()]
