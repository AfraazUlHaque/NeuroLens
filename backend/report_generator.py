import uuid
from datetime import datetime


class ReportGenerator:

    def __init__(self):
        pass


    def get_risk_level(self, tumor_percentage):

        if tumor_percentage == 0:
            return {
                "level": "No Tumor",
                "color": "Green"
            }

        elif tumor_percentage < 2:
            return {
                "level": "Low Risk",
                "color": "Green"
            }

        elif tumor_percentage < 10:
            return {
                "level": "Moderate Risk",
                "color": "Yellow"
            }

        else:
            return {
                "level": "High Risk",
                "color": "Red"
            }


    def generate(self, prediction):

        risk = self.get_risk_level(
            prediction["tumor_percentage"]
        )


        report = {

            "scan_id":
                str(uuid.uuid4())[:8].upper(),


            "date":
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M"
                ),


            "finding": (
                "Abnormal tumor region detected"
                if prediction["tumor_detected"]
                else "No abnormal region detected"
            ),


            "risk_level":
                risk["level"],


            "risk_color":
                risk["color"],


            "summary": (
                f"Tumor occupies "
                f"{prediction['tumor_percentage']}% "
                f"of analyzed MRI slice "
                f"with AI confidence "
                f"{prediction['confidence']}%."
            ),


            "disclaimer":
                "This AI-generated result is an assistance tool and not a medical diagnosis."
        }


        return report