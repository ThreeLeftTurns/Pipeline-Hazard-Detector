class Instruction:
    def __init__(self, operation, dest=None, src1=None, src2=None):
        self.operation = operation
        self.dest = dest
        self.src1 = src1
        self.src2 = src2

    def __repr__(self):
        return f"{self.operation} {self.dest} {self.src1} {self.src2}"


def detect_hazards(instructions):
    hazards = []
    pipeline = [{"inst": None, "stage": None} for _ in range(5)]
    timing = []
    for i in range(len(instructions) + 4):  # +4 for the pipeline length
        current_inst = instructions[i] if i < len(instructions) else None

        # Shift pipeline stages
        for j in range(4, 0, -1):
            pipeline[j] = pipeline[j - 1].copy()

        pipeline[0]["inst"] = current_inst
        pipeline[0]["stage"] = "IF"

        for j in range(min(i + 1, 5)):
            if pipeline[j]["stage"] == "IF":
                pipeline[j]["stage"] = "ID"
            elif pipeline[j]["stage"] == "ID":
                pipeline[j]["stage"] = "EX"
                # Detect hazard
                if pipeline[j]["inst"] and pipeline[j - 1]["inst"]:
                    if pipeline[j]["inst"].src1 == pipeline[j - 1]["inst"].dest or pipeline[j]["inst"].src2 == pipeline[j - 1]["inst"].dest:
                        hazards.append(f"RAW Hazard between {pipeline[j]['inst']} and {pipeline[j-1]['inst']}")
            elif pipeline[j]["stage"] == "EX":
                pipeline[j]["stage"] = "MEM"
            elif pipeline[j]["stage"] == "MEM":
                pipeline[j]["stage"] = "WB"

        timing.append([p["stage"] for p in pipeline])

    return hazards, timing


if __name__ == '__main__':
    instructions = [
        Instruction("lw", "R1", "R2"),
        Instruction("add", "R3", "R1", "R4"),
        Instruction("sub", "R5", "R6", "R1"),
        Instruction("sw", "R1", "R7")
    ]

    hazards, timing_sequence = detect_hazards(instructions)
    print("Hazards Detected:")
    for hazard in hazards:
        print(hazard)

    print("\nTiming Sequence (without any solution):")
    for seq in timing_sequence:
        print(seq)
