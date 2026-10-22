#!/usr/bin/env python3
"""Generates the static portfolio site into the output dir given as argv[1]."""
import os, sys, html

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
M = "https://static.wixstatic.com/media/"
def img(id_): return M + id_

SITE = "Karthik Karumanchi"
LINKEDIN = "https://linkedin.com/in/kmkar31"
GITHUB = "https://github.com/kmkar31"
RESUME = "https://686e8b1f-e8dd-4e34-9c3c-5ccc4d7af65d.filesusr.com/ugd/84da68_6a1c4dc4a15a4d4389d6b6b6fa727665.pdf"
PROFILE = img("84da68_7ddf4665a50c46ddabbf0ea3eec595b2~mv2.jpg")

ICON_LI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.8v1.54h.05c.53-1 1.82-2.05 3.75-2.05 4 0 4.75 2.63 4.75 6.05V21h-4v-5.1c0-1.22-.02-2.78-1.7-2.78-1.7 0-1.96 1.33-1.96 2.69V21h-4z"/></svg>'
ICON_GH = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 .5a11.5 11.5 0 0 0-3.64 22.41c.58.1.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.52-1.33-1.28-1.68-1.28-1.68-1.04-.71.08-.7.08-.7 1.15.08 1.76 1.19 1.76 1.19 1.03 1.76 2.69 1.25 3.35.96.1-.75.4-1.25.73-1.54-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.28 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.77 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.83 1.19 3.09 0 4.42-2.69 5.39-5.25 5.68.41.36.78 1.06.78 2.14v3.17c0 .31.21.67.8.56A11.5 11.5 0 0 0 12 .5z"/></svg>'

# ---------------------------------------------------------------- projects
def fig(src, cap="", alt="", cls=""):
    c = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure class="{cls}"><img src="{img(src)}" alt="{html.escape(alt or cap)}" loading="lazy">{c}</figure>'

def row(*figs): return '<div class="fig-row">' + "".join(figs) + "</div>"

PROJECTS = [
 dict(slug="snake-robots", title="Gait-based Control of Modular Snake Robots",
  q="How do we coordinate the motion of hyper-redundant snake robots while remaining computationally inexpensive?",
  thumb="84da68_68a480733b8146feb7ff1fad23072b9d~mv2.jpg", page_title="Snake Robots",
  desc="Projects on control of modular snake robots as part of the Biorobotics Lab, CMU.",
  body=f"""
<p>Snake robots are highly articulated robots that can coordinate their many degrees of freedom to access areas which are otherwise unreachable by machinery. They possess an infinite number of configurations allowing them to conform to and locomote over irregular terrain.</p>
<p>Read more about modular snake robots <a href="https://biorobotics.ri.cmu.edu/research/BiologicallyInspiredRobots.php" target="_blank" rel="noopener">here</a>.</p>
{row(fig("84da68_a5113b3b20964268a2cdd86d62ae636d~mv2.png", alt="Snake robot project"), fig("84da68_e3c936de1b1a46ceb67595fe49cd0916~mv2.png", alt="Snake robot project"), fig("84da68_3757d950eb33495fa760ec4e52ce2fe4~mv2.png", alt="Snake robot project"))}
"""),
 dict(slug="argus-mission", title="ARGUS Mission",
  q="How do we localize a satellite's position solely using visual methods?",
  thumb="84da68_dc84e56af31f48c2975157ca1d0a7b58~mv2.jpg", page_title="ARGUS Mission",
  desc="A nanosatellite designed to perform orbit determination using visual methods.",
  body=f"""
<p>Localizing a satellite's position in LEO is hard. GPS has export restrictions and large ground stations are expensive. ARGUS aims to use visual based orbit determination, i.e., using images of Earth to identify its position.</p>
{fig("84da68_d561ef950eb448809236d27460e6052e~mv2.jpg", alt="ARGUS mission")}
"""),
 dict(slug="quadrotor-landing", title="Quadrotor Landing on an Unstable Mobile Platform",
  q="How do we land aerial vehicles on mobile platforms in the presence of environmental disturbances?",
  thumb="84da68_3767353ce606470db6978bad6b77b7f3~mv2.jpg", page_title="Quadrotor Landing",
  desc="Finite State Machine based high-level controller for a quadrotor to autonomously navigate to and land on an unstable mobile platform.",
  body=f"""
<p>In the realm of robotics, navigating uncertain real-world environments presents significant challenges. Uncertainties occur in the form of rough seas, turbulent winds, etc. This project addresses these uncertainties in operating aerial vehicles in such unpredictable conditions. While existing autopilot systems can manage stable environments, they falter in windy conditions and on unstable landing platforms, requiring human intervention. To address these challenges, a novel algorithm was developed to land a quadrotor (the CrazyFlie) on a two-wheeled platform (the Tumbller) while the latter follows a trajectory, mimicking the difficulties of landing on a ship in rough seas.</p>
{fig("84da68_3767353ce606470db6978bad6b77b7f3~mv2.jpg", "Tumbller with the small landing pad (left) and the CrazyFlie (right)", "Project hardware: CrazyFlie drone and Tumbller landing platform")}
<p>The controller divided the CrazyFlie's maneuver into two phases: the search and land phase. Each phase operated an individual high-level model predictive controller to track the landing platform. Selecting the appropriate phase and generating the objectives was handled by a finite state machine. A secondary disturbance-rejection controller was implemented on the Tumbller to implement trajectory-following. The position of the Tumbller during its trajectory was made available to the CrazyFlie via a global positioning system. Since the trajectory was not made known to the CrazyFlie in advance, a "trajectory-prediction" subroutine was built in, allowing the CrazyFlie to make anticipatory maneuvers.</p>
<p>In the test, the Tumbller moves in a circular trajectory of radius 0.8 m at 0.38 m/s. The CrazyFlie takes off from a random location, navigates to the origin and then starts to track the Tumbller.</p>
<p>The control algorithm was tested with two landing pads mounted on the Tumbller. The smaller landing pad offered a 50% greater tolerance for error but caused 30% lower platform instability compared to the larger landing pad. The implemented control algorithm achieves a 100% rate of landing success with the smaller landing pad as long as the Tumbller is stable and moving slower than 0.25 m/s. When the Tumbller is moving at its highest speed of 0.38 m/s, the drone completed a successful landing in 5.6 s with a position error of 2.5 cm. However, challenges arose with the larger landing pad, as heightened platform instability caused fluctuation in position estimates, compromising controller performance.</p>
{fig("84da68_c0b0953450704f3ab136ef72e2d63fad~mv2.jpg", "Smaller landing pad (left) and the larger landing pad (right)", "Two landing pads to compare the effect of instability")}
<p>With the large landing pad, the Tumbller executes a circular trajectory of radius 0.8 m at 0.18 m/s and shows significant instability, affecting the CrazyFlie's accuracy.</p>
"""),
 dict(slug="raftar-formula-racing", title="Raftar Formula Racing",
  q="How do we build an electric racecar that is one-fifth the weight of a Ferrari but matches its 0-60 acceleration time?",
  thumb="84da68_2f4866a7d377424f8b71ef3d12529617~mv2.jpg", page_title="Raftar Formula Racing",
  desc="An electric Formula SAE car built by a team of 45 engineers at IIT Madras.",
  body=f"""
<p>Raftar Formula Racing is the FSAE team of IIT Madras. A team of 40+ engineering students design, build, test and race an electric formula-style car at Indian and European competitions.</p>
<p>Read more about the team <a href="https://www.raftariitm.com/" target="_blank" rel="noopener">here</a>.</p>
{row(fig("84da68_6dc1a48fd9e240f18c13004eedbfb4b1~mv2.webp", alt="Raftar Formula Racing car"), fig("84da68_601857af9385447db7042112e16c3e30~mv2.png", alt="Raftar Formula Racing"))}
"""),
 dict(slug="hasselhoff-submarine", title="Hasselhoff Submarine",
  q="How do we develop a submarine for underwater target detection?",
  thumb="84da68_c24e062c23de44129b5ec12fadd6e607~mv2.webp", page_title="Hasselhoff Submarine",
  desc="A fun game using a submarine to navigate to and land on a target.",
  body=f"""
<p>The Hasselhoff Bot is a small submarine inspired by David Hasselhoff's cameo in the 2004 SpongeBob Movie. In the movie, SpongeBob and Patrick explore the ocean in search of King Neptune's crown to cover his shiny, bald head and David Hasselhoff is the last "vehicle" that propels the two friends back to Bikini Bottom, where they return the crown to King Neptune. In a similar fashion, the Hasselhoff Bot is a small, user-steerable submarine that allows the user 99 seconds to explore an underwater environment in search of an IR beam mounted on the bottom of the tank.</p>
{row(fig("84da68_c24e062c23de44129b5ec12fadd6e607~mv2.webp", alt="Hasselhoff submarine"), fig("84da68_ffefc35738fe40f5a4bca7df529d1fd3~mv2.webp", alt="Remote controller for the Hasselhoff submarine"))}
<p class="cap">Hasselhoff submarine (left) and remote control (right)</p>
<h2>User Experience</h2>
<p>In its welcome state, the submarine spins in place and the remote flashes LEDs waiting for user interaction. When the user interacts with the joystick, the sub is set into drive mode and the user has 99 seconds to reach the target. The user may use the throttle and steering joysticks to control planar motion as well as the target depth knob to control the sub's depth. Once over the target, a blue light illuminates, allowing the user to "land" onto the target. The user is scored on how fast they can maneuver to the goal. Once the landing is done, the sub resurfaces and resumes its welcome state.</p>
<h2>Design Methodology</h2>
<p>The sub is powered by four waterproof thrusters driven by BLDC motors arranged radially. Two thrusters provide planar control and two provide ballast control. The motors are powered by a 4s1p 5000 mAh 21700 battery pack. All communications are executed via SPI. Processing, both on the submarine and the remote, is done using an STM32 microcontroller. The submarine is fitted with a depth sensor as well as an IR receiver. Waterproofing is done using gaskets and bolts arranged circumferentially. Electrical connections are passed via Deutsch and MPT connectors to prevent water leaks.</p>
{row(fig("84da68_4da2e6bf703d4ee48e1d1b202fe5389c~mv2.png", alt="Submarine external CAD schematic"), fig("84da68_a88077295ae7480ab3fc1653ff780517~mv2.png", alt="Submarine internal CAD schematic"))}
<p class="cap">Submarine CAD (external and internal schematics)</p>
<h2>State Machine Logic</h2>
<p>The submarine, remote and communications all operate on state machines where events are handled by linked lists. The remote uses a non-preemptive scheduler to add events to the linked list. Every command generated by the remote is sent to the submarine via SPI. Each SPI message is acknowledged by the submarine with an 8 bit submarine state which includes flags for target detection, land completion and sub status.</p>
{fig("84da68_bbba3759dc9948c88def0894c224682d~mv2.png", "Submarine state machine", "Submarine state machine logic")}
<h2>Testing</h2>
<p>The submarine was found to be waterproof when submerged in a 50 gal water tank. Within this small tub of water, the submarine was able to run through its states and demo the full user experience. Due to access limitations, the submarine has not yet been tested in a large body of water.</p>
{fig("84da68_df211b32362e4065ac840ce55d646095f000.jpg", "The sub being driven around in a 50 gal tub, commanded to spin in a circle using only a steering input", "Submarine testing in a tub", "narrow")}
<h2>Source Code</h2>
<p><a href="https://github.com/scott-wade/hasselhoff-bot" target="_blank" rel="noopener">GitHub repo</a></p>
"""),
 dict(slug="aerobraking-drl", title="Deep Reinforcement Learning for Aerobraking Maneuvers",
  q="How do we eliminate the reliance on human decisions during orbital insertions on other planets?",
  thumb="84da68_c839ad691caa43eba5f0fd8c6c2a7b22~mv2.gif", page_title="Aerobraking",
  desc="Deep reinforcement learning methods to automate spacecraft aerobraking maneuvers.",
  body=f"""
<p>Aerobraking is a technique that uses a planet's atmosphere to alter a spacecraft's trajectory from an interplanetary hyperbolic path to a target elliptical orbit. Current methods for conducting aerobraking maneuvers rely on continuous ground station monitoring, which introduces delays due to the vast distances involved in interplanetary travel. To address these challenges, this project implements a reinforcement learning approach for executing lightweight control strategies onboard. Our method trains a Proximal Policy Optimization (PPO) agent to perform aerobraking maneuvers faster and with reduced fuel consumption.</p>
{fig("84da68_fcee06d18ae44b0d83cb16d7137cc758~mv2.png", "Depiction of an aerobraking maneuver. An initial propulsive maneuver inserts the spacecraft into a high energy elliptical orbit from an interplanetary hyperbolic orbit. Subsequent passages through the atmosphere reduce the spacecraft's energy until a suitable target orbit is reached.", "Aerobraking maneuver definition")}
<p>As shown in the figure above, an initial propulsive maneuver moves the spacecraft from a hyperbolic interplanetary trajectory into a high-energy elliptical orbit whose periapsis (the orbit's near point) is in the planet's atmosphere. Repeated passages through the atmosphere (called drag passages) reduce the orbit's energy until a suitable apoapsis radius is reached. Then, additional propulsive maneuvers are executed to bring the periapsis out of the planet's atmosphere and stabilize the orbit. Control inputs are provided as &Delta;V's at the apoapses. These maneuvers raise or lower the periapsis and result in increased or decreased drag effect.</p>
<p>This project builds off work done by <a href="http://dx.doi.org/10.2514/6.2022-2497" target="_blank" rel="noopener">Falcone et al.</a> to develop an aerobraking agent simulating the Mars Odyssey orbit insertion mission. The spacecraft's state is depicted by the orbital elements of its current orbit: apoapsis radius, periapsis altitude, inclination, AOP (argument of periapsis) and RAAN (right ascension of the ascending node). The action space is a set of &Delta;V's that can be applied at each apoapsis: A = [&minus;1.0, &minus;0.5, &minus;0.3, &minus;0.2, &minus;0.1, &minus;0.05, 0, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0]. Negative actions lower the periapsis while positive actions raise it.</p>
<p>Every aerobraking episode begins with an initial apoapsis radius of 10038 km. The episode terminates when one of three conditions occurs: (a) the spacecraft attains or surpasses the target apoapsis radius of 4906 km, (b) the periapsis altitude falls below 85 km, below which it is bound to crash into the planet's surface, or (c) the periapsis altitude exceeds 135 km, beyond which atmospheric drag is negligible.</p>
{fig("84da68_145f9899d7964da680e9f15253708b4f~mv2.png", "A neural network based system model used to model spacecraft physics. The model was found to be accurate to within 1 km of the physics based model. The red lines represent the physics based model and the green lines represent the NN model.", "Neural network based state-space model")}
<p>Falcone et al. simulated their agent on a high-fidelity physics-based simulator. Due to the complex physics involved, the authors required a training time of 1 week on a 50 core cluster. To reduce training time, a neural network based system model was trained on the results of the physics based simulator. The trained model was accurate to within 1 km of the physics-based results, as shown in the figure above.</p>
<p>The most important part of a reinforcement learning based solution is the reward formulation. As shown below, a combination of a continuous and terminal reward function was used to provide the agent with continuous feedback. The agent is penalized on the normalized distance to the target and the magnitude of the action used.</p>
{row(fig("84da68_5c0cf947947a4c6ba2791e7929a9c20f~mv2.png", alt="Continuous reward function definition", cls="plain"), fig("84da68_01116cd2a7d14a4fa1a629570e846f90~mv2.png", alt="Terminal reward function formulation", cls="plain"))}
<p>The policy was represented by a neural network with 4 hidden layers and 512 hidden neurons per layer. The policy took the current state as input and gave the softmax-probabilities of each action in the action space. An action was randomly sampled weighted by these probabilities and applied on the system. Policy updates were clipped to 0.2 to maintain the sampling assumptions.</p>
<p>After training the PPO agent over 1.1 million steps (where each step is an action applied at the apoapsis, a subsequent drag passage and finally a return to the new apoapsis) with a batch size of 512 steps, the trained agent returned an average episodic reward of +5 with a terminal error of 8.4 km.</p>
{row(fig("84da68_65c1b9f82d1540bc88334b9aa0353d12~mv2.png", alt="PPO agent episode length over training steps"), fig("84da68_2b92e643d56c4d3b9b831220e5c674b5~mv2.png", alt="PPO agent average episodic return over training steps"))}
<p class="cap">Average episode length (number of propulsive maneuvers) (left) and the average episodic return (right) over number of training steps. The agent stabilizes around a return of +5 after 200,000 steps of training.</p>
{fig("84da68_2993bc0429fb432699aadf033f971d08~mv2.png", "Action-use space: the average number of times an action is used across a maneuver. In line with the goal to reduce fuel consumption, the agent mostly uses actions close to 0 (no propulsive maneuvers).", "PPO agent action selection frequency")}
<p>To verify the model against the actual physics based simulator, the inputs computed by the agent were fed into the simulator and the output was observed. Due to the high accuracy of our NN state-space model, the provided inputs succeeded in bringing the spacecraft to a target orbit, as shown below.</p>
{fig("84da68_510b1aad89ee43d491ea928d05b0d143~mv2.png", "Performance of the PPO agent on the physics based simulator. The agent brings the spacecraft to its target apoapsis radius within 46 orbits.", "PPO agent validation over physics based simulator")}
{fig("84da68_601bc70e80684a3b8e8979739a3a03c8~mv2.png", alt="Comparison of traditional and RL based methods", cls="plain")}
<p>To conclude, an RL-based method guarantees a successful aerobraking maneuver with lower fuel consumption and maneuver time compared to traditional human-involved decision making.</p>
"""),
 dict(slug="tethered-nanosatellite", title="Dynamics and Control of Tethered Nanosatellites",
  q="How do we use satellites to de-orbit space debris and clear up Low-Earth Orbit?",
  thumb="84da68_68cf50c42cec4973a058e0b5b33b664a~mv2.png", page_title="Tethered Nanosatellite",
  desc="Demonstrating the effectiveness of electrodynamic tethers in clearing debris from LEO.",
  body=f"""
<p>Kessler's Syndrome is a phenomenon where the increasing amount of satellite debris in orbit causes a cascading effect rendering orbits unusable. The US Space Surveillance Network reportedly tracks nearly 40,000 objects in orbit, monitoring them for potential threats to ongoing missions. These debris are classified into three categories (cars, hubcaps and shrapnel) based on their size. Cars are the largest and account for less than 1% of all debris. Shrapnel, on the other hand, is no larger than 1 cm and accounts for 98% of space debris. Cars, while low in number, pose a large threat since they can potentially break into millions of pieces of shrapnel.</p>
{fig("84da68_683f6cd5ca99486abd282f55566bb60b~mv2.jpg", 'A demonstration of Kessler&rsquo;s syndrome. Source: <a href="https://spectrum.ieee.org/weve-already-passed-the-tipping-point-for-orbital-debris" target="_blank" rel="noopener">We&rsquo;ve Already Passed the Tipping Point for Orbital Debris</a>, IEEE Spectrum', "Depiction of orbital debris")}
<p>Can we use satellites to de-orbit these "cars" and prevent Kessler's syndrome from occurring? Fuel-based de-orbiting procedures are far too expensive since they require a large amount of propellant to be carried from Earth. As an alternative, electrodynamic tethers (EDTs) use the Earth's magnetic field and properties of its outer atmosphere to deorbit debris. This project aims to demonstrate the use of EDTs in deorbiting space debris.</p>
{fig("84da68_68cf50c42cec4973a058e0b5b33b664a~mv2.png", "Electrodynamic tethers work by running a current through a thin strip of metal. This current interacts with the Earth's magnetic field, producing a drag force on the satellite.", "Electrodynamic tethers", "tall")}
<p>We do so by launching a 3U-1U CubeSat system connected by a thin aluminum tether 500 m long. The 1U satellite has a Spindt array that emits electrons. Earth's ionosphere has free ions which flow into the tether, completing a circuit and causing a current. Due to the Earth's magnetic field, the presence of a current in the tether causes a Lorentz drag force on it, reducing its orbital velocity. As its orbital velocity reduces, it moves closer and closer to the Earth, until it burns up in the atmosphere. Prior to launch, the 1U "daughter" satellite is housed within the 3U "mother" satellite. Once in orbit, a pin-puller mechanism generates an impulse, separates the two satellites and extends the tether.</p>
{fig("84da68_2cd876c1e7e74e7a8fb302ba48d8acb0~mv2.png", "3U mother satellite (left) and the 1U daughter satellite (right). The daughter satellite is housed within the mother satellite until they are inserted into orbit.", "Mother and daughter nanosatellites")}
<p>Due to the long length of the tether, gravitational variations cause the satellite system to oscillate about the mean point (called libration). This oscillation was damped by implementing B-dot control on the satellite system using magnetorquers. To design the satellite and its onboard electronics, the satellite was simulated in orbit to estimate the solar power incident on the solar panels. The thermal profile was also calculated to protect onboard electronics from failures.</p>
{fig("84da68_4399a65e25f947b095b6952a01397297~mv2.png", 'A magnetorquer board (source: <a href="https://www.cubesatshop.com/product/isis-magnetorquer-board/" target="_blank" rel="noopener">CubeSatShop</a>). The boards work by passing currents through solenoids. The solenoids generate magnetic fields which interact with the Earth&rsquo;s field to create torques.', "Magnetorquer board")}
"""),
 dict(slug="quadrotor-sysid", title="Grey-box System Identification of Quadrotors",
  q="How do we build accurate yet lightweight mathematical models for our system?",
  thumb="84da68_723a55c38d2b4c018aaa96108c047e1b~mv2.png", page_title="Grey-box System Identification",
  desc="Physics-rooted data-driven models to mathematically relate a quadrotor's power input to change in its global location.",
  body=f"""
<p>An object's movement is always described relative to a fixed point and a direction, known as a frame of reference. Typically, we use our surroundings as a frame of reference, which is called a global frame. However, we also use a local frame, based on our own position, when we describe direction using terms like "behind me" or "to my left." While robots operate in a global frame, their actuators work in a local frame, requiring a conversion of local movements into global displacements.</p>
<p>This is where a system model becomes crucial. For example, in the case of a drone, a system model considers local factors like roll, pitch, yaw, and thrust, converting them into global displacements along the X, Y, and Z axes. However, developing such models presents challenges, as they assume an ideal system-environment interaction that rarely exists in reality. Additionally, even with these assumptions, the resulting model is often so complex that it requires substantial computing power to use effectively.</p>
{fig("84da68_6df0228202e74535a5f452c999309ba2~mv2.png", "Local and global frames of reference in a quadrotor", "Quadrotor axis system")}
<p>To address these challenges, data-driven approaches have been developed, where the system operates in the real world and its state information is stored. This data is then used to mathematically identify relationships between input and output, without relying on physical principles. However, this approach can lead to unwanted variable relationships due to a lack of knowledge about the underlying physics. To mitigate these issues, grey-box system identification is employed, where a symbolic physics-based model is built and test data is fit to this symbolic model.</p>
<p>The objective of this project is to create a model of a quadrotor that calculates global displacement in the global frame based on local rotation angles and rotor power input. By applying propeller theory, 3D rotation theory, and Lagrangian mechanics, a system model is constructed, requiring the estimation of four constants representing gains along the three rotations and thrust.</p>
{row(fig("84da68_b6c64d60aa0c44b19ef20fe814c32e4e~mv2.png", alt="Translational dynamics", cls="plain"), fig("84da68_72654718edb04cd1924bca0ff0f755df~mv2.png", alt="Rotational dynamics", cls="plain"))}
<p class="cap">Physics-based symbolic system model. V represents the system bus voltage and the P's are individual %PWM inputs to the rotors. The coefficients C<sub>t</sub>, C<sub>roll</sub>, C<sub>pitch</sub> and C<sub>yaw</sub> have to be estimated using data-driven methods.</p>
{row(fig("84da68_70750168931845fd892e43d1dc83aeea~mv2.png", alt="Thrust coefficient estimation"), fig("84da68_8ee9aca3e5634025b98b8b4e406feff2~mv2.png", alt="Roll coefficient estimation"))}
<p class="cap">Results of the C<sub>t</sub> and C<sub>roll</sub> identification tests. C<sub>t</sub> is calculated by commanding the drone to hover (thrust = weight) and recording the power inputs to each rotor. C<sub>roll</sub> is computed by commanding a sinusoidal roll angle and calculating the roll acceleration.</p>
<p>The three rotational coefficients are determined by commanding a sinusoidal rotation along a specific axis and recording the global displacements. The thrust coefficient is obtained by conducting a hover test and measuring the point at which the rotor thrust balances the drone's weight.</p>
{row(fig("84da68_6ea167d03a7740e7bbd4c7df13191557~mv2.png", alt="Pitch coefficient estimation"), fig("84da68_4e0bfc31b3dd4d1095e207905b2e2d50~mv2.png", alt="Yaw coefficient estimation"))}
<p class="cap">Results of the C<sub>pitch</sub> and C<sub>yaw</sub> identification tests. Both coefficients are computed by commanding sinusoidal angles and calculating the corresponding accelerations.</p>
<p>The final system model is obtained as:</p>
{fig("84da68_39971515bfcb45c592a26725ba55f972~mv2.png", alt="Resultant system model", cls="plain")}
"""),
 dict(slug="assistive-tricycle", title="Design of an Assistive Tricycle",
  q="How do we design a tricycle that can be pedaled using a single leg without causing joint pain?",
  thumb="84da68_05d5033f23aa415484de4567ce426e30~mv2.png", page_title="Assistive Tricycle",
  desc="Design of an assistive tricycle to enhance mobility of persons with single-leg disabilities.",
  body=f"""
<p>This project aims to design a tricycle to be used by persons with lower-limb disabilities who possess full function in only one leg. To achieve this, specific criteria were established for the tricycle's design:</p>
<ol>
<li>Enable single-leg pedaling at a speed of 12 km/h.</li>
<li>Maintain affordability and durability.</li>
<li>Facilitate easy assembly and repair at standard bicycle repair shops.</li>
<li>Ensure narrow dimensions for maneuverability in small streets.</li>
<li>Withstand bumps and potholes commonly encountered on Indian roads.</li>
</ol>
{fig("84da68_6b1eba26356441ba8754b5b6ca57f636~mv2.png", alt="Design mind map")}
<p>Following a design flowchart analysis, it was determined that the pedaling mechanism design was of utmost importance.</p>
<p>Utilizing existing Indian anthropometric data and user studies, the maximum knee force and range of motion were determined. Traditional circular sprocket designs were found to exceed the knee's range of motion (ROM), potentially causing discomfort. To mitigate this issue, an elliptical pedaling mechanism employing a four-bar mechanism was devised.</p>
{row(fig("84da68_b99313c890554ddeb385961db61fb0d3~mv2.gif", "Knee ROM with a circular sprocket mechanism", "Circular mechanism knee angle range"), fig("84da68_c2791845e11147b8b6adb5e2f6066969~mv2.gif", "Knee ROM with the proposed elliptical mechanism", "Elliptical mechanism knee angle range"))}
<p>Through a grid-search optimization process, link lengths for the four-bar mechanism were fine-tuned while adhering to Grashof's criterion. Ultimately, a sprocket ratio of 2 was chosen, reducing the required force to acceptable levels. Despite a slightly faster cadence compared to circular mechanisms, it remained within user study parameters.</p>
<p>Moreover, it was discovered that knee range of motion depended not only on seat height but also on horizontal seat position. To accommodate a wide range of users, a dual adjustable seat was developed.</p>
<p>Given the single-leg pedaling limitation, a flywheel was integrated into the pedaling mechanism to release stored energy during the latter half of the pedaling cycle.</p>
<p>Safety was ensured through ANSYS FEA simulations, subjecting all components to fatigue, 3g bump, and 2g torsional loading. Subsequently, all parts were assembled using Autodesk Inventor, and production and assembly drawings were prepared.</p>
{row(fig("84da68_f4c07fc4120945f79eb0202dc25ff55f~mv2.jpg", alt="FEA of the frame in 3g bump loading"), fig("84da68_56c3a8aea23f456bb6afb1afa16f520a~mv2.jpg", alt="FEA of the frame in static loading"), fig("84da68_63b44453b60d4b4284c1febb4993a751~mv2.jpg", alt="FEA of the frame in 2g torsional loading"))}
<p class="cap">Deformation of the frame under static (left), 3g bump (center) and 2g torsional loading (right) respectively.</p>
{row(fig("84da68_fe921c32beae496d840313b6092b718f~mv2.jpg", alt="FEA of the rear sprocket adapter: deformation"), fig("84da68_e3bc0775e7db4eab8ceca22bc1747f54~mv2.jpg", alt="FEA of the rear sprocket adapter: stress"))}
<p class="cap">Deformation and stress on the rear sprocket adapter. The sprocket adapter performs three functions: it acts as a rear brake rotor, it transmits power from the rear sprocket to the driveshafts, and it also acts as a flywheel.</p>
"""),
]

# ---------------------------------------------------------------- redesign layout
META = {
 "snake-robots": dict(tags=["Robotics", "Controls"], tldr="Gait-based control that lets a many-jointed snake robot move through rough terrain without heavy computation.",
   results=[("Lab", "CMU Biorobotics"), ("Focus", "Compliant control")]),
 "argus-mission": dict(tags=["Space"], tldr="A nanosatellite concept that works out where it is by looking at Earth, with no GPS or ground station needed.",
   results=[("Approach", "Visual orbit determination"), ("Orbit", "LEO")]),
 "quadrotor-landing": dict(tags=["Robotics", "Controls"], tldr="A drone that finds, tracks and lands on a moving, wobbling platform using model predictive control and a state machine.",
   results=[("Landing success", "100% (small pad, under 0.25 m/s)"), ("At top speed", "5.6 s, 2.5 cm error")]),
 "raftar-formula-racing": dict(tags=["Build"], tldr="An electric Formula SAE racecar designed, built and raced by 40+ students at IIT Madras.",
   results=[("Team", "40+ engineers"), ("Result", "Podium, Formula Bharat 2023")]),
 "hasselhoff-submarine": dict(tags=["Robotics", "Build"], tldr="A waterproof, joystick-driven mini submarine that races a 99-second clock to land on a hidden IR target.",
   results=[("Thrusters", "4 BLDC"), ("Round length", "99 seconds")]),
 "aerobraking-drl": dict(tags=["Space", "Controls"], tldr="A reinforcement learning agent that flies a spacecraft into orbit around another planet on its own, using less fuel.",
   results=[("Terminal error", "8.4 km"), ("Training", "1.1M steps"), ("To target", "46 orbits")]),
 "tethered-nanosatellite": dict(tags=["Space", "Controls"], tldr="Using a 500 m conductive tether and Earth's magnetic field to drag dead satellites out of orbit.",
   results=[("Tether", "500 m"), ("Satellites", "3U + 1U CubeSat")]),
 "quadrotor-sysid": dict(tags=["Controls", "Robotics"], tldr="A physics-based drone model with just four constants, fitted from flight data.",
   results=[("Unknowns", "4 coefficients"), ("Method", "Grey-box ID")]),
 "assistive-tricycle": dict(tags=["Build"], tldr="A low-cost tricycle with an elliptical pedaling mechanism so one-legged riders can pedal without knee pain.",
   results=[("Target speed", "12 km/h"), ("Sprocket ratio", "2"), ("Checked with", "ANSYS FEA")]),
}
FILTERS = ["Robotics", "Controls", "Space", "Build"]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap" rel="stylesheet">'
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='16' fill='%23111827'/%3E%3Ctext x='32' y='43' font-family='sans-serif' font-size='32' font-weight='700' fill='%2322d3ee' text-anchor='middle'%3EK%3C/text%3E%3C/svg%3E"
ARROW = '<svg class="arrow" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M13 6l6 6-6 6"/></svg>'
SUN = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2"/><path stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MOON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg>'

def chips(tags): return "".join(f'<span class="chip">{t}</span>' for t in tags)

def page(fname, title, desc, body, active):
    nav = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{t}</a>'
        for k, h, t in [("home", "index.html", "Home"), ("about", "about.html", "About"), ("projects", "projects.html", "Projects")])
    full = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#0b1020">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{PROFILE}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{FAVICON}">
{FONTS}
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <a class="brand" href="index.html"><span class="mark">K</span><span class="brand-name">Karthik Karumanchi</span></a>
  <nav aria-label="Main">{nav}</nav>
  <div class="header-tools">
    <a class="icon-btn" href="{LINKEDIN}" target="_blank" rel="noopener" aria-label="LinkedIn">{ICON_LI}</a>
    <a class="icon-btn" href="{GITHUB}" target="_blank" rel="noopener" aria-label="GitHub">{ICON_GH}</a>
    <button class="icon-btn" id="theme" type="button" aria-label="Toggle light and dark theme"><span class="i-sun">{SUN}</span><span class="i-moon">{MOON}</span></button>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="footer-inner">
    <div>
      <p class="footer-title">Let&rsquo;s build something.</p>
      <p class="muted">Open to conversations about controls, robotics and autonomy.</p>
    </div>
    <div class="footer-links">
      <a class="btn" href="{LINKEDIN}" target="_blank" rel="noopener">{ICON_LI}<span>LinkedIn</span></a>
      <a class="btn ghost" href="{GITHUB}" target="_blank" rel="noopener">{ICON_GH}<span>GitHub</span></a>
      <a class="btn ghost" href="{RESUME}" target="_blank" rel="noopener"><span>Resume</span></a>
    </div>
  </div>
  <p class="copyright">&copy; Karthik Karumanchi</p>
</footer>
<div class="lightbox" id="lightbox" hidden><button type="button" aria-label="Close image" class="lb-close">&times;</button><img alt=""></div>
<script src="assets/site.js"></script>
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(full)

def card(p, big=False):
    m = META[p["slug"]]
    return f"""<a class="card reveal{' big' if big else ''}" href="{p['slug']}.html" data-tags="{' '.join(t.lower() for t in m['tags'])}">
  <div class="thumb"><img src="{img(p['thumb'])}" alt="{html.escape(p['title'])}" loading="lazy"></div>
  <div class="card-body">
    <div class="chips">{chips(m['tags'])}</div>
    <h3>{html.escape(p['title'])}</h3>
    <p>{html.escape(m['tldr'])}</p>
    <span class="more-link">View project {ARROW}</span>
  </div>
</a>"""

os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)

# ----------------------------------------------------------- home
featured = "".join(card(p) for p in PROJECTS[:6])
home = f"""
<section class="hero">
  <div class="blob b1"></div><div class="blob b2"></div>
  <div class="hero-inner">
    <div class="hero-text reveal">
      <p class="eyebrow"><span class="pulse"></span>Robotics &amp; Controls Engineer</p>
      <h1>I design the control systems that let machines <span class="grad">act on their own.</span></h1>
      <p class="lede">Hi, I&rsquo;m Karthik. I&rsquo;m a Master&rsquo;s student in Mechanical Engineering at Carnegie Mellon, researching compliant control of snake robots in the Biorobotics Lab under Prof. Howie Choset. Before that, I led IIT Madras&rsquo;s Formula SAE team to a podium finish.</p>
      <div class="actions">
        <a class="btn" href="projects.html">See my work {ARROW}</a>
        <a class="btn ghost" href="about.html">About me</a>
        <a class="btn ghost" href="{RESUME}" target="_blank" rel="noopener">Resume</a>
      </div>
    </div>
    <div class="portrait-wrap reveal">
      <img class="portrait" src="{PROFILE}" alt="Portrait of Karthik Karumanchi">
      <span class="badge bd1">Carnegie Mellon &middot; Biorobotics Lab</span>
      <span class="badge bd2">IIT Madras &rsquo;23</span>
    </div>
  </div>
</section>

<section class="stats reveal" aria-label="Highlights">
  <div><strong>4.0</strong><span>GPA at Carnegie Mellon</span></div>
  <div><strong>3 wk &rarr; 15 min</strong><span>Controller tuning time at Seagate</span></div>
  <div><strong>Podium</strong><span>Formula Bharat 2023, as team captain</span></div>
  <div><strong>9</strong><span>Projects across robots, satellites &amp; vehicles</span></div>
</section>

<section class="section">
  <div class="section-head reveal"><h2>Featured projects</h2><a class="more-link" href="projects.html">All projects {ARROW}</a></div>
  <div class="grid">{featured}</div>
</section>

<section class="section">
  <div class="section-head reveal"><h2>What I work on</h2></div>
  <div class="focus">
    <div class="focus-card reveal"><span class="num">01</span><h3>Control &amp; dynamics</h3><p>Model predictive control, adaptive and compliant control, and system identification: models that are accurate yet light enough to run on the robot.</p></div>
    <div class="focus-card reveal"><span class="num">02</span><h3>Learning for autonomy</h3><p>Reinforcement learning that replaces human-in-the-loop decisions, such as a PPO agent that flies aerobraking maneuvers around Mars.</p></div>
    <div class="focus-card reveal"><span class="num">03</span><h3>Hardware &amp; systems</h3><p>From CubeSats and a submarine to an electric racecar, designing, simulating, building and testing the real thing.</p></div>
  </div>
</section>
"""
page("index.html", "Karthik Karumanchi | Robotics and Controls Engineer",
     "Karthik Karumanchi - Master's Student in Mechanical Engineering at Carnegie Mellon University specializing in Robotics and Controls", home, "home")

# ----------------------------------------------------------- about
def tl(when, title, org, bullets=None, lines=None):
    inner = ""
    if lines: inner += "".join(f"<p>{l}</p>" for l in lines)
    if bullets: inner += "<ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>"
    return f"""<div class="tl-item reveal"><div class="tl-dot"></div><div class="tl-card"><p class="when">{when}</p><h3>{title}</h3><p class="org">{org}</p>{inner}</div></div>"""

skills = ["Model predictive control", "Reinforcement learning (PPO)", "System identification", "Adaptive &amp; compliant control",
          "B-dot attitude control", "Finite state machines", "Orbit, power &amp; thermal analysis", "FEA (ANSYS)", "CAD (Autodesk Inventor)",
          "Embedded systems (STM32, SPI)", "TCP/IP tooling"]
about = f"""
<section class="page-head"><div class="page-head-inner reveal">
  <p class="eyebrow">About</p>
  <h1>Engineering for autonomy, from first principles to hardware.</h1>
</div></section>
<section class="section narrow">
  <div class="about-top">
    <div class="prose reveal">
      <p>I&rsquo;m pursuing a Master&rsquo;s in Mechanical Engineering at Carnegie Mellon University. My goal is to push forward technological autonomy, with a focus on robotics and adaptive control. In the Biorobotics Lab, under <a href="https://www.ri.cmu.edu/ri-faculty/howie-choset/" target="_blank" rel="noopener">Prof. Howie Choset</a>, I&rsquo;ve implemented these algorithms on snake robots so they can traverse unknown terrain. I&rsquo;m also taking courses in robot learning and artificial intelligence.</p>
      <p>I earned my Bachelor&rsquo;s in Mechanical Engineering at the Indian Institute of Technology Madras. There I contributed to Raftar Formula Racing, modeling, designing and manufacturing the suspension and brakes for our institution&rsquo;s first electric racecar, the RFR23. In my senior year, I led the team to a podium finish at Formula Bharat 2023.</p>
      <p><a class="btn small" href="{RESUME}" target="_blank" rel="noopener">Download resume (PDF)</a></p>
    </div>
    <img class="portrait reveal" src="{PROFILE}" alt="Portrait of Karthik Karumanchi">
  </div>

  <h2 class="reveal">Skills &amp; tools</h2>
  <div class="chips big-chips reveal">{"".join(f'<span class="chip">{s}</span>' for s in skills)}</div>

  <h2 class="reveal">Education</h2>
  <div class="timeline">
    {tl("2023 &ndash; 2025", "MS Mechanical Engineering", "Carnegie Mellon University &middot; Pittsburgh, PA",
        lines=["<strong>Research:</strong> Compliant control of snake robots, Biorobotics Lab", "<strong>Courses:</strong> Advanced Control Systems Integration, Intro to Robot Learning", "<strong>GPA:</strong> 4.0 / 4.0"])}
    {tl("2019 &ndash; 2023", "B.Tech Mechanical Engineering", "Indian Institute of Technology Madras &middot; Chennai, India",
        lines=["<strong>Courses:</strong> Optimal Control, Multibody Dynamics, System Identification", "<strong>Activities:</strong> Captain of Raftar Formula Racing, the Formula SAE team of IIT Madras", "<strong>GPA:</strong> 9.3 / 10 (3.9 / 4.0)"])}
  </div>

  <h2 class="reveal">Experience</h2>
  <div class="timeline">
    {tl("May &ndash; Aug 2024", "Advanced Control Engineer Intern", "Seagate Technology &middot; Shakopee, MN",
        bullets=["Built a tool that simulates HDD head tiering tests, so track-follow controllers can be tuned without the factory in the loop.",
                 "Designed a server-client architecture over JSON-formatted TCP/IP so the tool is accessible globally.",
                 "Cut controller design iteration time on a batch of 30 drives from <strong>3 weeks to 15 minutes</strong>."])}
    {tl("May &ndash; Aug 2022", "MITACS Globalink Research Intern", "York University &middot; Toronto, Canada",
        bullets=["Implemented a pin-puller mechanism to reliably provide the impulse that deploys a 3U CubeSat in LEO.",
                 "Found the CubeSat&rsquo;s power limits by computing the solar energy incident on it in orbit.",
                 "Defined the operating temperature range in orbit to guide the satellite&rsquo;s electronic design requirements."])}
    {tl("Jun &ndash; Jul 2021", "Mechanical Simulations Intern", "Tube Investments India Ltd. &middot; Chennai, India",
        bullets=["Evaluated the safety of an electric three-wheeler&rsquo;s rear axle under 3g impulse loading.",
                 "Predicted transmission fluid leakage from failure of specific gearbox flange bolts under that load.",
                 "Recommended larger bolts and higher pretension to reduce failure risk and improve safety."])}
  </div>
</section>
"""
page("about.html", "About | Karthik Karumanchi", "Education and Professional Experience of Karthik Karumanchi", about, "about")

# ----------------------------------------------------------- projects index
filters = '<button class="filter active" data-filter="all" type="button">All</button>' + "".join(
    f'<button class="filter" data-filter="{t.lower()}" type="button">{t}</button>' for t in FILTERS)
projects = f"""
<section class="page-head"><div class="page-head-inner reveal">
  <p class="eyebrow">Projects</p>
  <h1>Robots, satellites and racecars, each starting with a question.</h1>
  <div class="filters" role="group" aria-label="Filter projects">{filters}</div>
</div></section>
<section class="section">
  <div class="grid" id="project-grid">{"".join(card(p) for p in PROJECTS)}</div>
  <p class="empty" id="empty" hidden>No projects match that filter.</p>
</section>
"""
page("projects.html", "Projects | Karthik Karumanchi", "Projects by Karthik Karumanchi at Carnegie Mellon University and IIT Madras", projects, "projects")

# ----------------------------------------------------------- project pages
for i, p in enumerate(PROJECTS):
    m = META[p["slug"]]
    res = "".join(f'<div><span>{k}</span><strong>{v}</strong></div>' for k, v in m["results"])
    prev_p, next_p = PROJECTS[i - 1], PROJECTS[(i + 1) % len(PROJECTS)]
    body = f"""
<section class="proj-hero">
  <div class="proj-hero-bg" style="background-image:url('{img(p['thumb'])}')"></div>
  <div class="proj-hero-inner reveal">
    <a class="crumb" href="projects.html">&larr; All projects</a>
    <div class="chips">{chips(m['tags'])}</div>
    <h1>{html.escape(p['title'])}</h1>
    <p class="question">{html.escape(p['q'])}</p>
    <p class="tldr">{html.escape(m['tldr'])}</p>
  </div>
</section>
<section class="section narrow">
  <div class="results reveal">{res}</div>
  <article class="prose project">
  {p['body']}
  </article>
  <nav class="pager" aria-label="More projects">
    <a href="{prev_p['slug']}.html"><span>&larr; Previous</span><strong>{html.escape(prev_p['title'])}</strong></a>
    <a href="{next_p['slug']}.html" class="next"><span>Next &rarr;</span><strong>{html.escape(next_p['title'])}</strong></a>
  </nav>
</section>
"""
    page(p["slug"] + ".html", f"{p['page_title']} | {SITE}", p["desc"], body, "projects")

page("404.html", "Page not found | Karthik Karumanchi", "Page not found",
     '<section class="page-head"><div class="page-head-inner"><p class="eyebrow">404</p><h1>That page doesn&rsquo;t exist.</h1><p class="actions"><a class="btn" href="index.html">Back home</a></p></div></section>', "")

# ----------------------------------------------------------- css
css = r"""
:root{
  --bg:#f6f7fb; --bg2:#eef0f7; --fg:#0f172a; --muted:#566074; --line:#dfe3ee; --card:#ffffff;
  --a1:#0e7490; --a2:#6d4aff; --grad:linear-gradient(120deg,#0e7490,#6d4aff);
  --glass:rgba(246,247,251,.78); --shadow:0 10px 30px rgba(15,23,42,.08); --shadow-lg:0 22px 50px rgba(15,23,42,.16);
  --radius:18px; --maxw:1160px;
}
:root[data-theme="dark"]{
  --bg:#0b1020; --bg2:#10172b; --fg:#e8ecf6; --muted:#9aa5bd; --line:#1f2a45; --card:#121a30;
  --a1:#22d3ee; --a2:#a78bfa; --grad:linear-gradient(120deg,#22d3ee,#a78bfa);
  --glass:rgba(11,16,32,.72); --shadow:0 10px 30px rgba(0,0,0,.35); --shadow-lg:0 22px 50px rgba(0,0,0,.55);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0b1020; --bg2:#10172b; --fg:#e8ecf6; --muted:#9aa5bd; --line:#1f2a45; --card:#121a30;
    --a1:#22d3ee; --a2:#a78bfa; --grad:linear-gradient(120deg,#22d3ee,#a78bfa);
    --glass:rgba(11,16,32,.72); --shadow:0 10px 30px rgba(0,0,0,.35); --shadow-lg:0 22px 50px rgba(0,0,0,.55);
  }
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.7 Inter,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:clip}
img{max-width:100%;height:auto;display:block}
a{color:var(--a1);text-underline-offset:3px}
h1,h2,h3{font-family:"Space Grotesk",Inter,system-ui,sans-serif;line-height:1.12;letter-spacing:-.02em;margin:0 0 .5em}
h1{font-size:clamp(2.1rem,5.2vw,3.7rem)}
h2{font-size:clamp(1.5rem,3vw,2.1rem);margin-top:2.2em}
h3{font-size:1.2rem}
.muted{color:var(--muted)}
.skip{position:absolute;left:-999px;top:8px;background:var(--fg);color:var(--bg);padding:8px 14px;border-radius:8px;z-index:100}
.skip:focus{left:8px}
:focus-visible{outline:3px solid var(--a1);outline-offset:3px;border-radius:6px}

/* header */
.site-header{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:20px;padding:12px max(20px,calc((100vw - var(--maxw))/2));background:var(--glass);backdrop-filter:saturate(1.4) blur(14px);-webkit-backdrop-filter:saturate(1.4) blur(14px);border-bottom:1px solid var(--line)}
.brand{display:flex;align-items:center;gap:10px;color:var(--fg);text-decoration:none;font-family:"Space Grotesk",sans-serif;font-weight:700;margin-right:auto}
.mark{display:grid;place-items:center;width:34px;height:34px;border-radius:10px;background:var(--grad);color:#fff;font-weight:700}
.site-header nav{display:flex;gap:6px}
.site-header nav a{color:var(--muted);text-decoration:none;font-weight:500;font-size:.95rem;padding:8px 14px;border-radius:999px;transition:.2s}
.site-header nav a:hover{color:var(--fg);background:var(--bg2)}
.site-header nav a[aria-current]{color:var(--fg);background:var(--bg2)}
.header-tools{display:flex;gap:4px}
.icon-btn{display:grid;place-items:center;width:40px;height:40px;border-radius:12px;border:0;background:transparent;color:var(--muted);cursor:pointer;transition:.2s}
.icon-btn:hover{color:var(--fg);background:var(--bg2)}
.icon-btn svg{width:20px;height:20px}
#theme .i-moon{display:none}
:root[data-theme="dark"] #theme .i-sun{display:none}
:root[data-theme="dark"] #theme .i-moon{display:inline}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]) #theme .i-sun{display:none}
  :root:not([data-theme="light"]) #theme .i-moon{display:inline}
}

/* buttons / chips */
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 22px;border-radius:999px;background:var(--grad);color:#fff;text-decoration:none;font-weight:600;font-size:.95rem;border:1.5px solid transparent;transition:transform .2s,box-shadow .2s}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(109,74,255,.35)}
.btn.ghost{background:transparent;color:var(--fg);border-color:var(--line)}
.btn.ghost:hover{border-color:var(--a1);box-shadow:none}
.btn.small{padding:9px 18px;font-size:.88rem}
.btn svg{width:18px;height:18px}
.arrow{width:18px;height:18px;transition:transform .2s}
.btn:hover .arrow,.card:hover .arrow,.more-link:hover .arrow{transform:translateX(4px)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{display:inline-block;padding:3px 12px;border-radius:999px;background:var(--bg2);border:1px solid var(--line);color:var(--muted);font-size:.78rem;font-weight:500}
.big-chips .chip{font-size:.9rem;padding:7px 16px;color:var(--fg)}
.more-link{display:inline-flex;align-items:center;gap:6px;color:var(--a1);font-weight:600;text-decoration:none;font-size:.95rem}
.eyebrow{display:inline-flex;align-items:center;gap:10px;text-transform:uppercase;letter-spacing:.14em;font-size:.76rem;color:var(--a1);font-weight:600;margin:0 0 18px}
.pulse{width:9px;height:9px;border-radius:50%;background:var(--a1);box-shadow:0 0 0 0 var(--a1);animation:pulse 2.2s infinite}
@keyframes pulse{70%{box-shadow:0 0 0 10px transparent}100%{box-shadow:0 0 0 0 transparent}}

/* hero */
.hero{position:relative;overflow:hidden;padding:72px 20px 40px}
.blob{position:absolute;border-radius:50%;filter:blur(80px);opacity:.35;z-index:0;animation:float 14s ease-in-out infinite}
.b1{width:480px;height:480px;background:var(--a1);top:-160px;left:-120px}
.b2{width:520px;height:520px;background:var(--a2);top:40px;right:-180px;animation-delay:-6s}
@keyframes float{50%{transform:translate(40px,30px) scale(1.08)}}
.hero-inner{position:relative;z-index:1;max-width:var(--maxw);margin:0 auto;display:grid;grid-template-columns:1.5fr 1fr;gap:56px;align-items:center}
.grad{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.lede{color:var(--muted);font-size:1.12rem;max-width:60ch}
.actions{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.portrait-wrap{position:relative;justify-self:center;max-width:380px}
.portrait{width:100%;border-radius:28px;box-shadow:var(--shadow-lg);border:1px solid var(--line)}
.badge{position:absolute;padding:8px 14px;border-radius:999px;background:var(--glass);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid var(--line);font-size:.8rem;font-weight:600;box-shadow:var(--shadow);animation:bob 6s ease-in-out infinite}
.bd1{left:-28px;bottom:36px}
.bd2{right:-18px;top:28px;animation-delay:-3s}
@keyframes bob{50%{transform:translateY(-8px)}}

/* stats */
.stats{max-width:var(--maxw);margin:24px auto 0;padding:0 20px;display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.stats>div{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:22px 20px;box-shadow:var(--shadow)}
.stats strong{display:block;font-family:"Space Grotesk",sans-serif;font-size:1.7rem;line-height:1.1;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.stats span{display:block;margin-top:6px;color:var(--muted);font-size:.88rem;line-height:1.4}

/* sections */
.section{max-width:var(--maxw);margin:0 auto;padding:56px 20px}
.section.narrow{max-width:860px}
.section-head{display:flex;align-items:baseline;justify-content:space-between;gap:16px;margin-bottom:26px}
.section-head h2{margin:0}
.page-head{padding:64px 20px 8px;background:linear-gradient(180deg,var(--bg2),transparent)}
.page-head-inner{max-width:var(--maxw);margin:0 auto}
.page-head h1{max-width:20ch}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin-top:28px}
.filter{border:1px solid var(--line);background:var(--card);color:var(--muted);padding:8px 18px;border-radius:999px;font:inherit;font-size:.9rem;font-weight:500;cursor:pointer;transition:.2s}
.filter:hover{color:var(--fg);border-color:var(--a1)}
.filter.active{background:var(--grad);color:#fff;border-color:transparent}
.empty{color:var(--muted);text-align:center;padding:40px 0}

/* cards */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:24px}
.card{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;color:inherit;text-decoration:none;box-shadow:var(--shadow);transition:transform .25s,box-shadow .25s,border-color .25s}
.card:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);border-color:color-mix(in srgb,var(--a1) 50%,var(--line))}
.card .thumb{aspect-ratio:16/10;overflow:hidden;background:var(--bg2)}
.card .thumb img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.card:hover .thumb img{transform:scale(1.06)}
.card-body{display:flex;flex-direction:column;gap:10px;padding:20px 22px 24px;flex:1}
.card h3{margin:0}
.card p{margin:0;color:var(--muted);font-size:.93rem;line-height:1.55}
.card .more-link{margin-top:auto;padding-top:6px}
.card[hidden]{display:none}

/* focus */
.focus{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px}
.focus-card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:28px;box-shadow:var(--shadow)}
.focus-card .num{font-family:"Space Grotesk",sans-serif;font-weight:700;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.focus-card h3{margin:.5em 0 .4em}
.focus-card p{margin:0;color:var(--muted);font-size:.95rem}

/* about */
.about-top{display:grid;grid-template-columns:1.6fr 1fr;gap:40px;align-items:start;margin-top:8px}
.about-top .portrait{max-width:300px;justify-self:center}
.prose p{margin:0 0 1.1em}
.timeline{position:relative;margin-top:24px;padding-left:28px}
.timeline:before{content:"";position:absolute;left:7px;top:8px;bottom:8px;width:2px;background:var(--line)}
.tl-item{position:relative;margin-bottom:22px}
.tl-dot{position:absolute;left:-28px;top:26px;width:16px;height:16px;border-radius:50%;background:var(--bg);border:3px solid var(--a1)}
.tl-card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:22px 26px;box-shadow:var(--shadow)}
.tl-card .when{margin:0 0 4px;color:var(--a1);font-size:.82rem;font-weight:600;letter-spacing:.04em;text-transform:uppercase}
.tl-card h3{margin:0}
.tl-card .org{margin:2px 0 10px;color:var(--muted)}
.tl-card p{margin:.25em 0}
.tl-card ul{margin:.4em 0 0;padding-left:1.2em}
.tl-card li{margin:.4em 0}

/* project page */
.proj-hero{position:relative;overflow:hidden;padding:56px 20px 64px;border-bottom:1px solid var(--line)}
.proj-hero-bg{position:absolute;inset:-30px;background-size:cover;background-position:center;filter:blur(36px) saturate(1.2);opacity:.28;transform:scale(1.1)}
.proj-hero:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,var(--bg))}
.proj-hero-inner{position:relative;z-index:1;max-width:860px;margin:0 auto}
.crumb{display:inline-block;margin-bottom:22px;color:var(--muted);text-decoration:none;font-size:.92rem;font-weight:500}
.crumb:hover{color:var(--a1)}
.question{font-size:1.25rem;color:var(--muted);font-style:italic;margin:.4em 0 .8em}
.tldr{font-size:1.05rem;margin:0;max-width:60ch}
.results{display:flex;flex-wrap:wrap;gap:16px;margin:-34px 0 36px;position:relative;z-index:2}
.results>div{flex:1 1 180px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:16px 20px;box-shadow:var(--shadow)}
.results span{display:block;color:var(--muted);font-size:.78rem;text-transform:uppercase;letter-spacing:.08em}
.results strong{display:block;font-family:"Space Grotesk",sans-serif;font-size:1.15rem;margin-top:4px}
.project h2{margin-top:1.8em}
.project figure{margin:1.8em 0}
.project figure img{border-radius:14px;margin:0 auto;box-shadow:var(--shadow);cursor:zoom-in;border:1px solid var(--line)}
.project figure.plain img{border-radius:8px;background:#fff;padding:8px;box-shadow:none}
.project figure.narrow img{max-width:320px}
.project figure.tall img{max-height:520px;width:auto}
figcaption,.cap{color:var(--muted);font-size:.88rem;text-align:center;margin-top:.8em;line-height:1.5}
.fig-row{display:flex;flex-wrap:wrap;gap:18px;align-items:flex-start;justify-content:center;margin:1.8em 0 .4em}
.fig-row figure{flex:1 1 220px;margin:0}
.project ol,.project ul{padding-left:1.3em}
.pager{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:64px}
.pager a{display:block;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:18px 22px;text-decoration:none;color:var(--fg);transition:.2s}
.pager a:hover{border-color:var(--a1);transform:translateY(-3px);box-shadow:var(--shadow)}
.pager span{display:block;color:var(--muted);font-size:.82rem;margin-bottom:4px}
.pager strong{font-family:"Space Grotesk",sans-serif;font-size:1rem;line-height:1.3}
.pager .next{text-align:right}

/* footer */
.site-footer{margin-top:56px;border-top:1px solid var(--line);background:var(--bg2);padding:48px 20px 28px}
.footer-inner{max-width:var(--maxw);margin:0 auto;display:flex;flex-wrap:wrap;gap:24px;align-items:center;justify-content:space-between}
.footer-title{font-family:"Space Grotesk",sans-serif;font-size:1.7rem;font-weight:700;margin:0}
.footer-links{display:flex;flex-wrap:wrap;gap:10px}
.copyright{max-width:var(--maxw);margin:32px auto 0;color:var(--muted);font-size:.85rem}

/* lightbox */
.lightbox{position:fixed;inset:0;z-index:200;background:rgba(5,8,18,.88);display:grid;place-items:center;padding:24px;cursor:zoom-out}
.lightbox[hidden]{display:none}
.lightbox img{max-height:90vh;max-width:94vw;border-radius:10px;background:#fff}
.lb-close{position:absolute;top:14px;right:18px;border:0;background:transparent;color:#fff;font-size:2.4rem;cursor:pointer;line-height:1}

/* reveal */
.js .reveal{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}
.js .reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion: reduce){
  *{animation:none!important;transition:none!important}
  .js .reveal{opacity:1;transform:none}
  html{scroll-behavior:auto}
}

/* touch targets */
.brand{min-height:44px;min-width:44px;justify-content:center}
.more-link{min-height:44px}
.crumb{display:inline-flex;align-items:center;min-height:44px;margin-bottom:10px}
.icon-btn{width:44px;height:44px}
.filter{min-height:44px}
.site-header nav a{min-height:44px;display:inline-flex;align-items:center}

@media (max-width:860px){
  .hero-inner,.about-top{grid-template-columns:1fr}
  .hero{padding:40px 20px 24px}
  .hero-inner{gap:32px}
  .portrait-wrap{max-width:240px}
  .badge{display:none}
  .blob{animation:none;filter:blur(60px);opacity:.28}
  .b1{width:300px;height:300px;top:-120px;left:-100px}
  .b2{width:320px;height:320px;top:120px;right:-140px}
  .stats{grid-template-columns:repeat(2,1fr)}
}
@media (max-width:620px){
  body{font-size:16px}
  h1{font-size:clamp(1.9rem,8.4vw,2.4rem)}
  .site-header{gap:6px;padding:6px 12px}
  .brand-name{display:none}
  .site-header nav{flex:1;justify-content:center;gap:0}
  .site-header nav a{padding:0 12px;font-size:.92rem}
  .header-tools a.icon-btn{display:none}
  .lede{font-size:1rem;line-height:1.6}
  .actions{margin-top:22px}
  .actions{display:grid;grid-template-columns:1fr 1fr}
  .actions .btn{justify-content:center}
  .actions .btn:first-child{grid-column:1/-1}
  .stats{gap:10px;padding:0 16px}
  .stats>div{padding:16px 14px}
  .stats strong{font-size:1.35rem}
  .section{padding:40px 16px}
  .page-head{padding:40px 16px 4px}
  .proj-hero{padding:32px 16px 52px}
  .pager{grid-template-columns:1fr}
  .pager .next{text-align:left}
  .results{margin-top:-26px}
  .section-head{flex-wrap:wrap}
  .footer-inner{flex-direction:column;align-items:flex-start}
  .tl-card{padding:18px}
  .timeline{padding-left:22px}
  .tl-dot{left:-22px}
}
"""
with open(os.path.join(OUT, "assets", "style.css"), "w") as f:
    f.write(css.strip() + "\n")

# ----------------------------------------------------------- js
js = r"""
(function(){
  var d=document, root=d.documentElement;
  root.classList.add('js');

  // theme toggle
  var tb=d.getElementById('theme');
  if(tb){tb.addEventListener('click',function(){
    var cur=root.getAttribute('data-theme');
    if(!cur){cur=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}
    var next=cur==='dark'?'light':'dark';
    root.setAttribute('data-theme',next);
    try{localStorage.setItem('theme',next)}catch(e){}
  });}

  // scroll reveal
  var els=[].slice.call(d.querySelectorAll('.reveal'));
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});
    },{rootMargin:'0px 0px -8% 0px',threshold:.05});
    els.forEach(function(el,i){el.style.transitionDelay=Math.min((i%6)*60,300)+'ms';io.observe(el);});
  } else { els.forEach(function(el){el.classList.add('in');}); }
  // safety net: never leave content hidden if the observer misses something
  setTimeout(function(){els.forEach(function(el){
    if(el.getBoundingClientRect().top<innerHeight*1.3){el.classList.add('in');}
  });},2500);
  addEventListener('load',function(){setTimeout(function(){els.forEach(function(el){
    if(el.getBoundingClientRect().top<innerHeight){el.classList.add('in');}
  });},300);});

  // project filter
  var fs=d.querySelectorAll('.filter');
  if(fs.length){
    var cards=d.querySelectorAll('#project-grid .card'), empty=d.getElementById('empty');
    fs.forEach(function(b){b.addEventListener('click',function(){
      fs.forEach(function(x){x.classList.remove('active');});
      b.classList.add('active');
      var f=b.getAttribute('data-filter'), shown=0;
      cards.forEach(function(c){
        var ok=f==='all'||(' '+c.getAttribute('data-tags')+' ').indexOf(' '+f+' ')>-1;
        c.hidden=!ok; if(ok){shown++;c.classList.add('in');}
      });
      empty.hidden=shown>0;
    });});
  }

  // image lightbox
  var lb=d.getElementById('lightbox');
  if(lb){
    var lbi=lb.querySelector('img');
    d.addEventListener('click',function(e){
      var t=e.target;
      if(t.tagName==='IMG'&&t.closest('.project figure')){lbi.src=t.src;lbi.alt=t.alt;lb.hidden=false;}
      else if(!lb.hidden){lb.hidden=true;}
    });
    d.addEventListener('keydown',function(e){if(e.key==='Escape'){lb.hidden=true;}});
  }
})();
"""
with open(os.path.join(OUT, "assets", "site.js"), "w") as f:
    f.write(js.strip() + "\n")

print("built", len(os.listdir(OUT)), "files in", OUT)
