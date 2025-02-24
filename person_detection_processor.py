import asyncio
import os

from viam.logging import getLogger
from viam.robot.client import RobotClient
from viam.services.vision import VisionClient

LOGGER = getLogger(__name__)

robot_api_key = os.getenv('ROBOT_API_KEY')
robot_api_key_id = os.getenv('ROBOT_API_KEY_ID')
robot_address = os.getenv('ROBOT_ADDRESS')

# Define the component and service names from the Viam app CONFIGURE tab
vision_name = os.getenv('VISION_NAME')
camera_name = os.getenv('CAMERA_NAME')

async def connect():
    opts = RobotClient.Options.with_api_key(
      api_key=robot_api_key,
      api_key_id=robot_api_key_id
    )
    return await RobotClient.at_address(robot_address, opts)

async def main():
    machine = await connect()
    LOGGER.info(f"Launching Person Detector: {vision_name}")
    # person-detector
    person_detector = VisionClient.from_robot(machine, vision_name)

    N = 5
    for i in range(N):
        try:
            LOGGER.info(f"Iteration {i+1}/{N}")
            detections = await person_detector.get_detections_from_camera(camera_name)

            found = False
            for d in detections:
                LOGGER.info(f"Detection: class_name={d.class_name}, confidence={d.confidence}")
                if d.confidence > 0.8 and d.class_name.lower() == "person":
                    LOGGER.info("Person detected!")
                    found = True
                    break

            if found:
                LOGGER.info("Person detected.")

            else:
                LOGGER.info("No person detected.")

        except Exception as e:
            LOGGER.error(f"Error during loop iteration: {e}")

        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(main())
