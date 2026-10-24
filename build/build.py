#!/usr/bin/env python3
"""Generates the static portfolio site into the output dir given as argv[1]."""
import os, sys, html, json

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
    return f'<figure class="{cls}"><a class="zoom" href="{img(src)}"><img src="{img(src)}" alt="{html.escape(alt or cap)}" loading="lazy" decoding="async"></a>{c}</figure>'

def row(*figs): return '<div class="fig-row">' + "".join(figs) + "</div>"

PROJECTS = [
 dict(slug="snake-robots", title="Gait-based Control of Modular Snake Robots",
  q="How do we coordinate the motion of hyper-redundant snake robots while remaining computationally inexpensive?",
  thumb="84da68_68a480733b8146feb7ff1fad23072b9d~mv2.jpg", page_title="Snake Robots",
  desc="Gait-based, compliant controllers for modular snake robots, implemented in CMU's Biorobotics Lab so they can cross unknown terrain.",
  body=f"""
{row(fig("84da68_a5113b3b20964268a2cdd86d62ae636d~mv2.png", alt="Modular snake robot, figure 1 of 3"), fig("84da68_e3c936de1b1a46ceb67595fe49cd0916~mv2.png", alt="Modular snake robot, figure 2 of 3"), fig("84da68_3757d950eb33495fa760ec4e52ce2fe4~mv2.png", alt="Modular snake robot, figure 3 of 3"))}
<h2>Why snake robots</h2>
<p>A snake robot coordinates many joints at once, so it can reach places other machines cannot and conform to irregular terrain. Read more on the <a href="https://biorobotics.ri.cmu.edu/research/BiologicallyInspiredRobots.php" target="_blank" rel="noopener">CMU Biorobotics Lab research page</a>.</p>
"""),
 dict(slug="argus-mission", title="ARGUS Mission",
  q="How do we localize a satellite's position solely using visual methods?",
  thumb="84da68_dc84e56af31f48c2975157ca1d0a7b58~mv2.jpg", page_title="ARGUS Mission",
  desc="A nanosatellite that finds its own position in low Earth orbit from images of the Earth, avoiding GPS export limits and costly ground stations.",
  body=f"""
<p>Localizing a satellite's position in LEO is hard. GPS has export restrictions and large ground stations are expensive. ARGUS aims to use visual based orbit determination, i.e., using images of Earth to identify its position.</p>
{fig("84da68_d561ef950eb448809236d27460e6052e~mv2.jpg", alt="ARGUS nanosatellite mission figure")}
"""),
 dict(slug="quadrotor-landing", title="Quadrotor Landing on an Unstable Mobile Platform",
  q="How do we land aerial vehicles on mobile platforms in the presence of environmental disturbances?",
  thumb="84da68_3767353ce606470db6978bad6b77b7f3~mv2.jpg", page_title="Quadrotor Landing",
  desc="A CrazyFlie quadrotor lands on a moving Tumbller robot using model predictive control and a state machine: 100% success on the small pad below 0.25 m/s.",
  body=f"""
<p>Existing autopilots can manage stable environments, but they falter in wind and on unstable landing platforms, and then need a human to step in. This project built an algorithm to land a quadrotor (the CrazyFlie) on a two-wheeled platform (the Tumbller) while the latter follows a trajectory, mimicking the difficulties of landing on a ship in rough seas.</p>
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
  desc="Raftar Formula Racing, IIT Madras: 40+ students built and raced an electric Formula SAE car; podium at Formula Bharat 2023.",
  body=f"""
<p>Raftar Formula Racing is the FSAE team of IIT Madras. A team of 40+ engineering students design, build, test and race an electric formula-style car at Indian and European competitions.</p>
<p>Read more on the <a href="https://www.raftariitm.com/" target="_blank" rel="noopener">Raftar Formula Racing website</a>.</p>
{row(fig("84da68_6dc1a48fd9e240f18c13004eedbfb4b1~mv2.webp", alt="Raftar Formula Racing electric car"), fig("84da68_601857af9385447db7042112e16c3e30~mv2.png", alt="Raftar Formula Racing team figure"))}
"""),
 dict(slug="hasselhoff-submarine", title="Hasselhoff Submarine",
  q="How do we develop a submarine for underwater target detection?",
  thumb="84da68_c24e062c23de44129b5ec12fadd6e607~mv2.webp", page_title="Hasselhoff Submarine",
  desc="A mini submarine with four BLDC thrusters and a joystick remote: the player has 99 seconds to drive it onto an IR target.",
  body=f"""
<p>The Hasselhoff Bot is a small, user-steerable submarine that gives the user 99 seconds to explore an underwater environment in search of an IR beam mounted on the bottom of the tank. It is named for David Hasselhoff's cameo in the 2004 SpongeBob Movie, where he is the last "vehicle" that carries SpongeBob and Patrick back to Bikini Bottom.</p>
{row(fig("84da68_c24e062c23de44129b5ec12fadd6e607~mv2.webp", alt="The Hasselhoff submarine"), fig("84da68_ffefc35738fe40f5a4bca7df529d1fd3~mv2.webp", alt="Remote controller for the Hasselhoff submarine"))}
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
  desc="A PPO agent that picks the burns for an aerobraking orbit insertion; on a physics simulator it reaches the target orbit in 46 orbits.",
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
  desc="Two CubeSats joined by a 500 m electrodynamic tether that uses Earth's magnetic field to drag debris out of low Earth orbit.",
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
  desc="A physics-based quadrotor model with four unknown coefficients, fitted from hover and sinusoidal-rotation flight tests.",
  body=f"""
<p>The objective of this project is to create a model of a quadrotor that calculates global displacement in the global frame based on local rotation angles and rotor power input. By applying propeller theory, 3D rotation theory, and Lagrangian mechanics, a system model is constructed, requiring the estimation of four constants representing gains along the three rotations and thrust.</p>
<h2>The model and the tests</h2>
{row(fig("84da68_b6c64d60aa0c44b19ef20fe814c32e4e~mv2.png", alt="Translational dynamics", cls="plain"), fig("84da68_72654718edb04cd1924bca0ff0f755df~mv2.png", alt="Rotational dynamics", cls="plain"))}
<p class="cap">Physics-based symbolic system model. V represents the system bus voltage and the P's are individual %PWM inputs to the rotors. The coefficients C<sub>t</sub>, C<sub>roll</sub>, C<sub>pitch</sub> and C<sub>yaw</sub> have to be estimated using data-driven methods.</p>
{row(fig("84da68_70750168931845fd892e43d1dc83aeea~mv2.png", alt="Thrust coefficient estimation"), fig("84da68_8ee9aca3e5634025b98b8b4e406feff2~mv2.png", alt="Roll coefficient estimation"))}
<p class="cap">Results of the C<sub>t</sub> and C<sub>roll</sub> identification tests. C<sub>t</sub> is calculated by commanding the drone to hover (thrust = weight) and recording the power inputs to each rotor. C<sub>roll</sub> is computed by commanding a sinusoidal roll angle and calculating the roll acceleration.</p>
<p>The three rotational coefficients are determined by commanding a sinusoidal rotation along a specific axis and recording the global displacements. The thrust coefficient is obtained by conducting a hover test and measuring the point at which the rotor thrust balances the drone's weight.</p>
{row(fig("84da68_6ea167d03a7740e7bbd4c7df13191557~mv2.png", alt="Pitch coefficient estimation"), fig("84da68_4e0bfc31b3dd4d1095e207905b2e2d50~mv2.png", alt="Yaw coefficient estimation"))}
<p class="cap">Results of the C<sub>pitch</sub> and C<sub>yaw</sub> identification tests. Both coefficients are computed by commanding sinusoidal angles and calculating the corresponding accelerations.</p>
<p>The final system model is obtained as:</p>
{fig("84da68_39971515bfcb45c592a26725ba55f972~mv2.png", alt="Resultant system model", cls="plain")}
<h2>Background</h2>
<p>An object's movement is always described relative to a fixed point and a direction, known as a frame of reference. Typically, we use our surroundings as a frame of reference, which is called a global frame. However, we also use a local frame, based on our own position, when we describe direction using terms like "behind me" or "to my left." While robots operate in a global frame, their actuators work in a local frame, requiring a conversion of local movements into global displacements.</p>
<p>This is where a system model becomes crucial. For example, in the case of a drone, a system model considers local factors like roll, pitch, yaw, and thrust, converting them into global displacements along the X, Y, and Z axes. However, developing such models presents challenges, as they assume an ideal system-environment interaction that rarely exists in reality. Additionally, even with these assumptions, the resulting model is often so complex that it requires substantial computing power to use effectively.</p>
{fig("84da68_6df0228202e74535a5f452c999309ba2~mv2.png", "Local and global frames of reference in a quadrotor", "Quadrotor axis system")}
<p>To address these challenges, data-driven approaches have been developed, where the system operates in the real world and its state information is stored. This data is then used to mathematically identify relationships between input and output, without relying on physical principles. However, this approach can lead to unwanted variable relationships due to a lack of knowledge about the underlying physics. To mitigate these issues, grey-box system identification is employed, where a symbolic physics-based model is built and test data is fit to this symbolic model.</p>
"""),
 dict(slug="assistive-tricycle", title="Design of an Assistive Tricycle",
  q="How do we design a tricycle that can be pedaled using a single leg without causing joint pain?",
  thumb="84da68_05d5033f23aa415484de4567ce426e30~mv2.png", page_title="Assistive Tricycle",
  desc="A tricycle for riders with one working leg, designed for 12 km/h on an elliptical four-bar path, checked with ANSYS FEA.",
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


# ---------------------------------------------------------------- authored plates (line art drawn from facts already on each page)
import math
def _snake():
    pts=[(40+i*55, 100+42*math.sin(i*0.95)) for i in range(8)]
    seg="".join(f'<line x1="{a[0]:.0f}" y1="{a[1]:.0f}" x2="{b[0]:.0f}" y2="{b[1]:.0f}" class="thick"/>' for a,b in zip(pts,pts[1:]))
    j="".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="7" class="paper"/>' for x,y in pts)
    return f'{seg}{j}<path d="M40 176h425" class="dash"/><path d="M455 170l10 6-10 6" />'
def _orbits():
    es="".join(f'<ellipse cx="{205+k*0:.0f}" cy="100" rx="{rx}" ry="{ry}" class="{"acc" if k==0 else ""}"/>' for k,(rx,ry) in enumerate([(170,78),(138,64),(110,52),(86,42)]))
    return f'<circle cx="240" cy="100" r="30" class="paper"/><circle cx="240" cy="100" r="42" class="dash"/>{es.replace("205","240")}'
PLATES = {
 "snake-robots": (_snake(), "Schematic of a modular snake robot in a serpentine gait. Module count is illustrative.", "Eight joined modules following a sine-wave body shape"),
 "argus-mission": ('<path d="M-40 250 A330 330 0 0 1 520 250" class="paper"/><rect x="224" y="34" width="32" height="22" class="paper"/><path d="M200 40h24M256 40h24" class="thick"/><path d="M240 56L150 107M240 56L330 107" class="dash"/><path d="M150 107A330 330 0 0 1 330 107" class="acc thick"/><text x="240" y="170" text-anchor="middle">visible patch of Earth</text>',
   "A nanosatellite in low Earth orbit images the ground below it; the position estimate comes from those images alone, not GPS.", "Satellite looking down at a patch of Earth"),
 "quadrotor-landing": ('<circle cx="240" cy="100" r="70" class="dash"/><circle cx="240" cy="100" r="3" class="fill"/><text x="206" y="126">origin</text><rect x="283" y="46" width="30" height="30" class="paper acc" transform="rotate(35 298 61)"/><path d="M80 40l70 38 80 20" class="dash"/><path d="M70 40h20M80 30v20" class="thick"/><text x="20" y="22">start (random)</text><path d="M240 100h70" /><text x="258" y="122">r = 0.8 m</text>',
   "Top view of the test: the Tumbller drives a 0.8 m circle at 0.38 m/s while the CrazyFlie flies from a random start to the origin and then tracks it.", "Circular platform path with a quadrotor approaching from a random start"),
 "raftar-formula-racing": ('<circle cx="120" cy="140" r="34" class="paper"/><circle cx="120" cy="140" r="12"/><circle cx="360" cy="140" r="34" class="paper"/><circle cx="360" cy="140" r="12"/><path d="M60 128H30v-14h70M154 140h172M100 114L190 100 210 70h60l30 38 70 8v12" class="thick"/><path d="M215 70l-8-24h46l-6 24" /><path d="M20 176h440" class="dash"/>',
   "Side-on sketch of an open-wheel Formula SAE car, the kind the team built. I did the suspension and brakes.", "Open-wheel race car in side view"),
 "hasselhoff-submarine": ('<rect x="170" y="50" width="140" height="100" rx="40" class="paper"/><circle cx="150" cy="60" r="16" class="acc"/><circle cx="330" cy="60" r="16" class="acc"/><circle cx="150" cy="140" r="16" class="acc"/><circle cx="330" cy="140" r="16" class="acc"/><circle cx="415" cy="100" r="26" class="dash"/><circle cx="415" cy="100" r="10"/><circle cx="415" cy="100" r="2" class="fill"/><path d="M315 100H378" class="dash"/><text x="170" y="176">4 thrusters</text><text x="388" y="148">IR target</text>',
   "Top view: four thrusters drive the hull, and the pilot has 99 seconds to land it on the infrared target.", "Submarine seen from above with four thrusters, heading for a target ring"),
 "aerobraking-drl": (_orbits()+'<text x="352" y="36">46 orbits</text><path d="M240 100H410" class="dash"/>',
   "Each pass through the upper atmosphere shrinks the orbit. The agent picks the burns that bring it to the target in 46 orbits.", "Nested orbits shrinking around a planet"),
 "tethered-nanosatellite": ('<path d="M-60 330 A360 360 0 0 1 540 330" class="paper"/><text x="240" y="192" text-anchor="middle">Earth</text><rect x="224" y="108" width="32" height="26" class="paper"/><text x="266" y="126">3U</text><rect x="233" y="20" width="14" height="14" class="paper"/><text x="256" y="32">1U</text><path d="M240 34V108"/><path d="M206 34h20M206 108h20M216 34V108" class="dash"/><text x="262" y="76">500 m tether</text>',
   "A 3U and a 1U CubeSat joined by a 500 m tether, orbiting together. Not to scale.", "Two satellites linked by a long tether above the Earth"),
 "quadrotor-sysid": ('<path d="M40 30V170H450M40 100H450" /><path d="M40 100H190" class="acc thick"/><path d="M190 100C215 36 240 36 262 100S310 164 334 100S380 36 406 100" class="acc thick"/><text x="62" y="86">hover</text><text x="236" y="190">sinusoidal rotation</text><text x="48" y="24">signal</text><text x="424" y="190">t</text>',
   "The two test types used to fit the model: hover, then sinusoidal rotation.", "Plot with a flat hover trace followed by a sine wave"),
 "assistive-tricycle": ('<circle cx="170" cy="100" r="62" class="dash"/><ellipse cx="320" cy="100" rx="80" ry="48" class="acc thick"/><circle cx="170" cy="100" r="3" class="fill"/><circle cx="320" cy="100" r="3" class="fill"/><text x="116" y="186">circular</text><text x="274" y="186">elliptical</text>',
   "Foot path of a circular crank (dashed) against the elliptical four-bar path (solid) used to keep the knee within its range of motion.", "Circle beside a wider ellipse"),
}
def plate(slug):
    svg, cap, label = PLATES[slug]
    return f'<figure class="plate"><svg viewBox="0 0 480 200" role="img" aria-label="{html.escape(label)}">{svg}</svg><figcaption><b>Fig. 1</b> {html.escape(cap)}<span class="sheet">Sheet {[q["slug"] for q in PROJECTS].index(slug)+1} of {len(PROJECTS)} &middot; NTS</span></figcaption></figure>'

# ---------------------------------------------------------------- redesign layout
META = {
 "snake-robots": dict(tags=["Robotics", "Controls"], tldr="Compliant, gait-based controllers I implemented on modular snake robots in CMU's Biorobotics Lab so they can cross unknown terrain.",
   results=[("Lab", "CMU Biorobotics Lab"), ("Advisor", "Prof. Howie Choset")]),
 "argus-mission": dict(tags=["Space"], tldr="Can a satellite find its own position in low Earth orbit by looking at the Earth? GPS has export limits and ground stations are costly, so this one uses images.",
   results=[("Approach", "Visual orbit determination"), ("Orbit", "LEO")]),
 "quadrotor-landing": dict(tags=["Robotics", "Controls"], tldr="Landed a CrazyFlie on a Tumbller balancing robot driving in a circle, with model predictive control and a state machine.",
   results=[("Landing success", "100% (small pad, under 0.25 m/s)"), ("At top speed", "5.6 s, 2.5 cm error")]),
 "raftar-formula-racing": dict(tags=["Build"], tldr="IIT Madras's electric Formula SAE car, built and raced by 40+ students. I captained the team and did the suspension and brakes.",
   stamp="Podium, Formula Bharat 2023", results=[("Team", "40+ students"), ("Result", "Podium, Formula Bharat 2023")]),
 "hasselhoff-submarine": dict(tags=["Robotics", "Build"], tldr="A mini submarine named after David Hasselhoff's cameo in the SpongeBob Movie. Four thrusters, a joystick remote, and 99 seconds to land on the target.",
   stamp="Time allowed: 99 s", results=[("Thrusters", "4 BLDC"), ("Time allowed", "99 seconds")]),
 "aerobraking-drl": dict(tags=["Space", "Controls"], tldr="Trained a PPO agent to pick the burns for an aerobraking orbit insertion, then checked it on a physics simulator: target reached in 46 orbits.",
   stamp="46 orbits to target", results=[("Terminal error", "8.4 km"), ("Training", "1.1M steps"), ("To target", "46 orbits")]),
 "tethered-nanosatellite": dict(tags=["Space", "Controls"], tldr="Two CubeSats on a 500 m tether that use Earth's magnetic field to drag debris out of orbit.",
   results=[("Tether", "500 m"), ("Satellites", "3U + 1U CubeSat")]),
 "quadrotor-sysid": dict(tags=["Controls", "Robotics"], tldr="A physics-based quadrotor model with four unknown constants, which I fitted from hover and sinusoidal-rotation tests.",
   results=[("Unknowns", "4 coefficients"), ("Tests", "Hover and sinusoidal rotation")]),
 "assistive-tricycle": dict(tags=["Build"], tldr="A tricycle for riders with one working leg. The pedals follow an elliptical four-bar path so the knee stays within its range of motion.",
   results=[("Target speed", "12 km/h"), ("Sprocket ratio", "2"), ("Checked with", "ANSYS FEA")]),
}
FILTERS = ["Robotics", "Controls", "Space", "Build"]

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&amp;family=Source+Serif+4:ital,wght@0,400;0,600;1,400&amp;display=swap" rel="stylesheet">'
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23d9a441'/%3E%3Crect x='2' y='2' width='60' height='60' fill='none' stroke='%232b2118' stroke-width='4'/%3E%3Ctext x='32' y='46' font-family='Georgia,serif' font-size='40' fill='%232b2118' text-anchor='middle'%3EK%3C/text%3E%3C/svg%3E"
ARROW = '<svg class="arrow" viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M13 6l6 6-6 6"/></svg>'
SUN = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="2"/><path stroke="currentColor" stroke-width="2" stroke-linecap="round" d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MOON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round" d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg>'

def chips(tags): return "".join(f'<span class="chip">{t}</span>' for t in tags)

BASE = "https://kmkar31.github.io/website/"
OG = BASE + "assets/og.png"
PAGES = []

LIGHTBOX = '<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer" hidden><button type="button" aria-label="Close image" class="lb-close">&times;</button><img alt=""></div>'
# Owner to supply, e.g. "Graduated May 2025; open to roles in ...". Renders nothing while empty.
STATUS = ""

import subprocess
def lastmod(n):
    try:
        d = subprocess.run(["git", "log", "-1", "--format=%cs", "--", n], capture_output=True, text=True, cwd=OUT or ".").stdout.strip()
    except Exception:
        d = ""
    return f"<lastmod>{d}</lastmod>" if d else ""

def page(fname, title, desc, body, active, ld=None):
    PAGES.append(fname)
    URL = BASE if fname == "index.html" else BASE + fname
    ldtag = ("\n<script type=\"application/ld+json\">" + json.dumps(ld, ensure_ascii=False) + "</script>") if ld else ""
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
{'<meta name="robots" content="noindex">' + chr(10) if fname == "404.html" else ""}<meta name="theme-color" content="#efe7d6">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{OG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Karthik Karumanchi, robotics and controls engineer">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{html.escape(title)}">
<meta name="twitter:description" content="{html.escape(desc)}">
<meta name="twitter:image" content="{OG}">
<link rel="canonical" href="{URL}">
<link rel="icon" href="{FAVICON}">{ldtag}
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
    <a class="hdr-resume" href="{RESUME}" target="_blank" rel="noopener">Resume (PDF)<span class="sr-only"> (opens in a new tab)</span></a>
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
    <p>To get in touch, message me on LinkedIn.</p>
    <div class="footer-links">
      <a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a>
      <a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a>
      <a href="{RESUME}" target="_blank" rel="noopener">Resume (PDF)</a>
    </div>
  </div>
  <p class="copyright">&copy; Karthik Karumanchi. Set in DM Serif Display and Source Serif 4. Hand-built static pages, one stylesheet, no framework.</p>
</footer>
{LIGHTBOX if 'class="zoom"' in body else ""}
<script src="assets/site.js"></script>
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(full)

def row_item(p, thumb=False, first=False):
    m = META[p["slug"]]
    n = PROJECTS.index(p) + 1
    stamp = f'<span class="stamp s-{p["slug"].split("-")[0]}">{m["stamp"]}</span>' if m.get("stamp") else ""
    t = f'<span class="thumb"><img src="{img(p["thumb"])}" alt="" width="96" height="72" loading="lazy"></span>' if thumb else ""
    return f"""<li data-tags="{' '.join(x.lower() for x in m['tags'])}"><a class="row{' has-thumb' if thumb else ''}{' start' if first else ''}" href="{p['slug']}.html">{t}<span><h3>{html.escape(p['title'])}</h3><p>{html.escape(m['tldr'])}</p></span><span class="tags"><b class="no" aria-hidden="true">{n:02d}</b>{stamp}{('<span class="here">Start here</span>' if first else '')}{' / '.join(m['tags'])}</span></a></li>"""

os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)

PERSON = {"@context": "https://schema.org", "@type": "Person", "name": "Karthik Karumanchi", "url": BASE,
  "description": "Mechanical engineer working on control of robots and spacecraft.",
  "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Carnegie Mellon University"}, {"@type": "CollegeOrUniversity", "name": "Indian Institute of Technology Madras"}],
  "sameAs": [LINKEDIN, GITHUB]}

# ----------------------------------------------------------- home
home = f"""
<section class="intro">
  <h1>Karthik Karumanchi</h1>
  <p class="subhead">MS Mechanical Engineering, Carnegie Mellon University</p>
<div class="intro-grid"><div class="intro-text">
  <p class="lede">I work on control of robots and spacecraft. At CMU&rsquo;s Biorobotics Lab, under Prof. Howie Choset, I research compliant control of snake robots. Before that I captained the Formula SAE team at IIT Madras, which finished on the podium at Formula Bharat 2023.</p>
  <p class="lede">As an intern at Seagate I built a simulation tool that cut controller design iteration on a batch of 30 drives from <a class="hl" href="about.html#seagate"><span class="strike">three weeks</span> to 15 minutes</a>.</p>
  <div class="actions">
    <a class="btn" href="projects.html">See the projects</a>
    <span class="action-links"><a class="textlink" href="{RESUME}" target="_blank" rel="noopener">Resume (PDF)</a>
    <a class="textlink" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></span>
  </div>
</div>
<aside class="ledger" aria-label="Quick facts"><p class="ledger-h">For the record</p>
<dl>{f'<div><dt>Status</dt><dd>{STATUS}</dd></div>' if STATUS else ''}<div><dt>Built</dt><dd>Pin-puller for a 3U CubeSat, 2022</dd></div><div><dt>Internships</dt><dd>Seagate, York University, Tube Investments</dd></div><div><dt>Toolbox</dt><dd>MPC, PPO, system ID, STM32, ANSYS</dd></div></dl></aside>
</div>
</section>

<section class="section">
  <div class="section-head"><h2>Projects</h2></div>
  <ul class="index">{"".join(row_item(p, first=(i == 0)) for i, p in enumerate(PROJECTS))}</ul>
</section>
"""
page("index.html", "Karthik Karumanchi | Control of Robots and Spacecraft",
     "Karthik Karumanchi, MS Mechanical Engineering at Carnegie Mellon. Control of robots and spacecraft: snake robots, quadrotor landing, aerobraking.", home, "home", ld=PERSON)

# ----------------------------------------------------------- about
def tl(when, title, org, bullets=None, lines=None, id_=None):
    inner = ""
    if lines: inner += "".join(f"<p>{l}</p>" for l in lines)
    if bullets: inner += "<ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>"
    return f"""<div class="tl-item"{f' id="{id_}"' if id_ else ''}><p class="when">{when}</p><h3>{title}</h3><p class="org">{org}</p>{inner}</div>"""

skills = [("Control and learning", ["Model predictive control", "Reinforcement learning (PPO)", "Adaptive &amp; compliant control", "B-dot attitude control", "Finite state machines"]),
          ("Analysis", ["System identification", "Orbit, power &amp; thermal analysis", "FEA (ANSYS)"]),
          ("Build and software", ["CAD (Autodesk Inventor)", "Embedded systems (STM32, SPI)", "TCP/IP tooling"])]
about = f"""
<section class="page-head"><h1>About</h1></section>
<section class="section about">
  <div class="about-top">
    <div class="prose">
      <p>My Master&rsquo;s in Mechanical Engineering is at Carnegie Mellon University (2023 &ndash; 2025), with a focus on robotics and adaptive control. In the Biorobotics Lab, under <a href="https://www.ri.cmu.edu/ri-faculty/howie-choset/" target="_blank" rel="noopener">Prof. Howie Choset</a>, I&rsquo;ve implemented these algorithms on snake robots so they can traverse unknown terrain.</p>
      <p>I earned my Bachelor&rsquo;s in Mechanical Engineering at the Indian Institute of Technology Madras. There I contributed to Raftar Formula Racing, modeling, designing and manufacturing the suspension and brakes for our institution&rsquo;s first electric racecar, the RFR23. In my senior year, I led the team to a podium finish at Formula Bharat 2023.</p>
      <p><a class="btn small" href="{RESUME}" target="_blank" rel="noopener">Resume (PDF)</a></p>
    </div>
    <img class="portrait" src="{PROFILE}" alt="Portrait of Karthik Karumanchi">
    <aside class="ledger toc" aria-label="On this page"><p class="ledger-h">On this page</p><dl><div><dt><a href="#skills">Skills &amp; tools</a></dt></div><div><dt><a href="#education">Education</a></dt></div><div><dt><a href="#experience">Experience</a></dt></div></dl></aside>
  </div>

  <h2 id="skills">Skills &amp; tools</h2>
  <div class="skill-cols">{"".join(f'<div><h3 class="skill-group">{g}</h3><ul class="skills">' + "".join(f'<li>{x}</li>' for x in items) + '</ul></div>' for g, items in skills)}</div>

  <h2 id="education">Education</h2>
  <div class="timeline">
    {tl("2023 &ndash; 2025", "MS Mechanical Engineering", "Carnegie Mellon University &middot; Pittsburgh, PA",
        lines=["<strong>Research:</strong> Compliant control of snake robots, Biorobotics Lab", "<strong>Courses:</strong> Advanced Control Systems Integration, Intro to Robot Learning", "<strong>GPA:</strong> 4.0 / 4.0"])}
    {tl("2019 &ndash; 2023", "B.Tech Mechanical Engineering", "Indian Institute of Technology Madras &middot; Chennai, India",
        lines=["<strong>Courses:</strong> Optimal Control, Multibody Dynamics, System Identification", "<strong>Activities:</strong> Captain of Raftar Formula Racing, the Formula SAE team of IIT Madras", "<strong>GPA:</strong> 9.3 / 10 (3.9 / 4.0)"])}
  </div>

  <h2 id="experience">Experience</h2>
  <div class="timeline">
    {tl("May &ndash; Aug 2024", "Advanced Control Engineer Intern", "Seagate Technology &middot; Shakopee, MN",
        bullets=["Built a tool that simulates HDD head tiering tests, so track-follow controllers can be tuned without the factory in the loop.",
                 "Designed a server-client architecture over JSON-formatted TCP/IP so the tool is accessible globally.",
                 "Cut controller design iteration time on a batch of 30 drives from <strong><span class='strike'>3 weeks</span> to 15 minutes</strong>."], id_="seagate")}
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
page("about.html", "About Karthik Karumanchi: CMU MS, IIT Madras, Seagate intern", "Education and professional experience of Karthik Karumanchi: CMU, IIT Madras, Seagate, York University and Tube Investments.", about, "about", ld=PERSON)

# ----------------------------------------------------------- projects index
filters = '<button class="filter active" data-filter="all" type="button" aria-pressed="true">All</button>' + "".join(
    f'<button class="filter" data-filter="{t.lower()}" type="button" aria-pressed="false">{t}</button>' for t in FILTERS)
projects = f"""
<section class="page-head">
  <h1>Projects</h1>
  <div class="filters" role="group" aria-label="Filter projects">{filters}</div>
  <p class="sr-only" id="filter-status" role="status" aria-live="polite"></p>
</section>
<section class="section">
  <ul class="index" id="project-list">{"".join(row_item(p, True) for p in PROJECTS)}</ul>
  <p class="empty" id="empty" hidden>No projects match that filter.</p>
</section>
"""
page("projects.html", "Robotics, controls and space projects | Karthik Karumanchi", "Nine projects: snake robots, quadrotor landing, aerobraking, tethered nanosatellites, a Formula SAE car, a mini submarine and more, from CMU and IIT Madras.", projects, "projects", ld={"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": q["title"], "url": BASE + q["slug"] + ".html"} for i, q in enumerate(PROJECTS)]})

# ----------------------------------------------------------- project pages
def first_fact(slug):
    k, v = META[slug]['results'][0]
    return f'{k}: {v}'
for i, p in enumerate(PROJECTS):
    m = META[p["slug"]]
    res = "".join(f'<div{" class=stamped" if k == "Time allowed" else ""}><dt>{k}</dt><dd>{v}</dd></div>' for k, v in m["results"])
    prev_p, next_p = PROJECTS[i - 1], PROJECTS[(i + 1) % len(PROJECTS)]
    body = f"""
<section class="proj-hero">
  <a class="crumb" href="projects.html">&larr; all projects</a>
  <p class="tags">{' / '.join(m['tags'])}</p>
  <h1>{html.escape(p['title'])}</h1>
  <p class="tldr">{html.escape(m['tldr'])}</p>
  <p class="question"><span>The question</span> {html.escape(p['q'])}</p>
</section>
<section class="section narrow" style="padding-top:0">
  <dl class="facts">{res}</dl>
  <article class="prose project">
  {plate(p['slug'])}
  {p['body']}
  </article>
  <nav class="pager" aria-label="More projects">
    <a href="{prev_p['slug']}.html"><span>&larr; Previous</span><strong>{html.escape(prev_p['title'])}</strong><em>{html.escape(first_fact(prev_p['slug']))}</em></a>
    <a href="{next_p['slug']}.html" class="next"><span>Next &rarr;</span><strong>{html.escape(next_p['title'])}</strong><em>{html.escape(first_fact(next_p['slug']))}</em></a>
  </nav>
</section>
"""
    page(p["slug"] + ".html", f"{p['title']} | {SITE}", p["desc"], body, "projects",
         ld={"@context": "https://schema.org", "@type": "CreativeWork", "name": p["title"], "description": p["desc"],
             "url": BASE + p["slug"] + ".html", "author": {"@type": "Person", "name": "Karthik Karumanchi", "url": BASE}})

page("404.html", "Page not found | Karthik Karumanchi", "This page does not exist. Back to the project index.",
     '<section class="page-head"><h1>That page doesn&rsquo;t exist.</h1><p class="lede" style="margin-top:16px">This page failed to land on the target. Back to the index.</p><p class="actions"><a class="btn" href="index.html">Back home</a></p></section>', "")

with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{BASE if n == 'index.html' else BASE + n}</loc>{lastmod(n)}</url>\n" for n in PAGES if n != "404.html") + "</urlset>\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")

# ----------------------------------------------------------- css
css = r"""
:root{
  --bg:#efe7d6; --bg2:#e5dbc3; --fg:#2b2118; --muted:#5b4e40; --ink:#2b2118; --line:#b9ab8a; --card:#f7f1e3;
  --a1:#9c3a22; --a2:#2f6f62; --hi:#d9a441; --btn-bg:#b4452b; --btn-fg:#f7f1e3; --shadowc:#2b2118;
  --maxw:1040px; --grid:#e3d9c1; --band-bg:#2b2118; --band-fg:#efe7d6; --band-mute:#c9bca2; --band-link:#e8a652;
  --serif:"DM Serif Display",Georgia,"Times New Roman",serif;
  --text:"Source Serif 4",Georgia,"Times New Roman",serif;
  --sans:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:ui-monospace,Menlo,Consolas,monospace;
  --grain:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 .17 0 0 0 0 .13 0 0 0 0 .09 0 0 0 .16 0'/%3E%3C/filter%3E%3Crect width='160' height='160' filter='url(%23n)'/%3E%3C/svg%3E");
}
/* dark = inverted print: dark paper, tan ink rules, hard shadows go darker than the paper */
:root[data-theme="dark"]{
  --bg:#1f1a15; --bg2:#272019; --fg:#eadfc8; --muted:#d9cfba; --ink:#9a8c71; --line:#4f4436; --card:#2a231b;
  --a1:#e8a652; --a2:#7fc4b0; --hi:#d9a441; --btn-bg:#e8a652; --btn-fg:#1d1814; --shadowc:#0c0a08; --grid:#2d251c; --band-bg:#14100c; --band-fg:#eadfc8; --band-mute:#b8ab95; --band-link:#e8a652;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#1f1a15; --bg2:#272019; --fg:#eadfc8; --muted:#d9cfba; --ink:#9a8c71; --line:#4f4436; --card:#2a231b;
    --a1:#e8a652; --a2:#7fc4b0; --hi:#d9a441; --btn-bg:#e8a652; --btn-fg:#1d1814; --shadowc:#0c0a08; --grid:#2d251c;
  }
}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:80px}
body{margin:0;background:var(--bg) var(--grain);color:var(--fg);font:18px/1.6 var(--text);-webkit-font-smoothing:antialiased;overflow-x:clip}
img{max-width:100%;height:auto;display:block}
a{color:var(--a1);text-underline-offset:3px;text-decoration-thickness:1px}
h1,h2,h3{font-family:var(--serif);font-weight:400;line-height:1.1;letter-spacing:-.005em;margin:0 0 .5em}
h1{font-size:clamp(2.3rem,6vw,3.8rem)}
h2{font-size:clamp(1.6rem,3vw,2.1rem);margin-top:2em}
h3{font-size:1.3rem}
.muted{color:var(--muted)}
.skip{position:absolute;left:-999px;top:8px;background:var(--fg);color:var(--bg);padding:8px 14px;z-index:100}
.skip:focus{left:8px}
:focus-visible{outline:3px solid var(--a1);outline-offset:3px}

/* header: double rule underneath, like a printed masthead */
.site-header{position:sticky;top:0;z-index:50;display:flex;align-items:center;gap:20px;padding:6px max(20px,calc((100% - var(--maxw))/2 + 20px));background:var(--bg);border-bottom:5px double var(--ink);font-family:var(--sans)}
.brand{display:flex;align-items:center;gap:10px;color:var(--fg);text-decoration:none;font-family:var(--serif);font-size:1.25rem;margin-right:auto;min-height:44px;min-width:44px;justify-content:center}
.mark{display:grid;place-items:center;width:34px;height:34px;border:2px solid var(--ink);background:var(--hi);color:#2b2118;font-family:var(--serif);font-size:1.3rem;line-height:1}
.site-header nav{display:flex;gap:4px}
.site-header nav a{color:var(--fg);text-decoration:none;font-weight:500;font-size:.95rem;padding:0 12px;min-height:44px;display:inline-flex;align-items:center;border-bottom:3px solid transparent}
.site-header nav a:hover{border-color:var(--line)}
.site-header nav a[aria-current]{border-color:var(--a1)}
.header-tools{display:flex;gap:2px;align-items:center}
.hdr-resume{color:var(--fg);font:500 .95rem var(--sans);padding:0 12px;min-height:44px;display:inline-flex;align-items:center;text-decoration:none;border-bottom:3px solid transparent}
.hdr-resume:hover{border-color:var(--line)}
.icon-btn{display:grid;place-items:center;width:44px;height:44px;border:0;background:transparent;color:var(--fg);cursor:pointer}
.icon-btn:hover{color:var(--a1)}
.icon-btn svg{width:20px;height:20px}
#theme .i-moon{display:none}
:root[data-theme="dark"] #theme .i-sun{display:none}
:root[data-theme="dark"] #theme .i-moon{display:inline}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]) #theme .i-sun{display:none}
  :root:not([data-theme="light"]) #theme .i-moon{display:inline}
}

/* the only boxed, shadowed things: the primary button and filter buttons */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:12px 22px;min-height:46px;background:var(--btn-bg);color:var(--btn-fg);text-decoration:none;font:600 .95rem var(--sans);border:2px solid var(--ink);box-shadow:4px 4px 0 var(--shadowc);transition:transform .12s,box-shadow .12s}
.btn:hover{transform:translate(-2px,-2px);box-shadow:6px 6px 0 var(--shadowc)}
.btn:active{transform:translate(1px,1px);box-shadow:1px 1px 0 var(--shadowc)}
.btn.small{padding:9px 18px;min-height:44px;font-size:.9rem}
.btn svg{width:18px;height:18px}
.textlink{display:inline-flex;align-items:center;min-height:44px;color:var(--a1);font:500 .98rem var(--sans);padding:0 4px}
.tags{font-family:var(--mono);font-size:.78rem;color:var(--muted);letter-spacing:.02em}
.more-link{display:inline-flex;align-items:center;min-height:44px;color:var(--a1);font:500 .95rem var(--sans)}
.more-link:hover{background:var(--hi);color:#2b2118;text-decoration:none}
.hl{background:var(--hi);color:#2b2118;text-decoration:underline;text-decoration-thickness:1px;padding:0 3px}
.hl:hover{background:#2b2118;color:#f7f1e3}
.skill-group{font:600 .8rem var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:1.4em 0 .4em}
.skills{margin:0;padding:0;list-style:none;font-size:1rem}
.skills li{padding:5px 0;border-bottom:1px solid var(--line);break-inside:avoid}

/* intro (home) */
.intro{max-width:var(--maxw);margin:0 auto;padding:56px 20px 8px}
.intro h1{margin-bottom:.15em}
.subhead{font-family:var(--mono);font-size:.9rem;color:var(--muted);margin:0 0 26px}
.lede{font-size:1.2rem;max-width:34em;margin:0 0 1em}
.action-links{display:inline-flex;gap:6px 22px}
.actions{display:flex;flex-wrap:wrap;align-items:center;gap:6px 22px;margin-top:26px}

.strike{text-decoration:line-through;text-decoration-thickness:2px}
.intro-grid{display:grid;grid-template-columns:minmax(0,1fr) 270px;gap:24px 56px;align-items:start}
.ledger{border-top:3px solid var(--ink);padding-top:8px;font-family:var(--mono);font-size:.85rem}
.ledger-h{margin:0 0 4px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em;font-size:.75rem}
.ledger dl{margin:0}
.ledger dl div{padding:9px 0;border-bottom:1px solid var(--line)}
.ledger dt{color:var(--muted);font-size:.78rem}
.ledger dd{margin:1px 0 0;color:var(--fg);line-height:1.35}
.row .no{display:block;color:var(--fg);font-weight:700;font-size:.85rem;margin-bottom:2px}

/* sections */
.section{max-width:var(--maxw);margin:0 auto;padding:44px 20px}
.section.narrow{max-width:760px}
.section-head{display:flex;align-items:baseline;justify-content:space-between;gap:16px;margin-bottom:6px;border-bottom:3px solid var(--ink);padding-bottom:6px}
.section-head h2{margin:0}
.page-head{padding:48px 20px 12px;max-width:var(--maxw);margin:0 auto}
.page-head.narrow{max-width:760px}
.page-head h1{max-width:22ch;margin-bottom:0}
.filters{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.filter{border:2px solid var(--ink);background:var(--card);color:var(--fg);padding:0 18px;min-height:44px;font:500 .9rem var(--sans);cursor:pointer}
.filter:hover{background:var(--hi);color:#2b2118}
.filter.active{background:var(--fg);color:var(--bg)}
.empty{color:var(--muted);padding:24px 0}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

/* project index: ruled rows, like a table of contents */
.index{list-style:none;margin:0;padding:0}
.index li[hidden]{display:none}
.row{display:grid;grid-template-columns:1fr 240px;gap:8px 24px;align-items:baseline;padding:18px 8px;border-bottom:1px solid var(--line);color:inherit;text-decoration:none;min-height:44px}
.row.has-thumb{grid-template-columns:96px 1fr 240px;align-items:center}
.row.no-thumb{grid-template-columns:1fr 240px;align-items:baseline}
.row.no-thumb .thumb{display:none}
.row .thumb{width:96px;height:72px;border:1px solid var(--ink);background:var(--bg2);overflow:hidden}
.row .thumb img{width:100%;height:100%;object-fit:cover;filter:saturate(.85) sepia(.15)}
.row h3{margin:0 0 .15em;font-size:1.35rem}
.row p{margin:0;color:var(--fg);font-size:1rem;line-height:1.45;max-width:46em}
.row:hover{background:var(--card);box-shadow:inset 4px 0 0 var(--a1)}
.row:active{transform:translate(2px,2px)}
.row.start h3{font-size:1.65rem}
.tags .here{display:block;margin:0 0 6px;font:700 .72rem var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--fg);border-bottom:2px solid var(--a1);width:max-content}
.facts div.stamped dd{cursor:pointer;user-select:none;-webkit-user-select:none;touch-action:manipulation}
.filter:active{transform:translate(2px,2px)}
.row:hover h3{text-decoration:underline;text-decoration-thickness:1px}

/* figure plates: drawn from facts on the page, graph-paper ground like a lab notebook */
.project figure.plate{margin:0 0 1.8em;border:1px solid var(--ink);background-color:var(--card);background-image:linear-gradient(var(--grid) 1px,transparent 1px),linear-gradient(90deg,var(--grid) 1px,transparent 1px);background-size:20px 20px}
.plate svg{display:block;width:100%;height:auto;fill:none;stroke:var(--fg);stroke-width:2;stroke-linecap:round;stroke-linejoin:round;font:600 13px var(--mono)}
.plate text{fill:var(--fg);stroke:none}
.plate .paper{fill:var(--card)}
.plate .thick{stroke-width:5}
.plate .dash{stroke-dasharray:6 6;stroke-width:1.5}
.plate .acc{stroke:var(--a1)}
.plate .fill{fill:var(--fg)}
.plate figcaption{margin:0;padding:8px 12px;background:var(--bg);border-top:1px solid var(--ink)}
.plate figcaption{display:flex;flex-wrap:wrap;gap:2px 12px;align-items:baseline}
.plate .sheet{margin-left:auto;font:500 .72rem var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--muted,var(--fg))}
.plate figcaption b{font:700 .78rem var(--mono);letter-spacing:.06em;text-transform:uppercase;margin-right:8px}
@media (max-width:620px){.plate svg{font-size:16px}}

/* about */
.section.about .timeline,.section.about>h2{max-width:760px}
.section.about>h2{border-top:1px solid var(--line);padding-top:.6em;position:relative}
.about-top{display:grid;grid-template-columns:minmax(0,38em) 280px;gap:24px 56px;align-items:start}
.about-top.no-portrait .portrait{display:none}
.about-top .toc{display:none}
.about-top.no-portrait{grid-template-columns:minmax(0,38em) 280px}
.about-top.no-portrait .toc{display:block}
.toc dt a{display:flex;align-items:center;min-height:44px;color:var(--fg);text-decoration:none;font-size:.9rem}
.toc dt a:hover{color:var(--a1);text-decoration:underline}
.about-top .portrait{width:100%;max-width:280px;margin-top:.4em;border:1px solid var(--ink)}
.skill-cols{max-width:760px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0 40px}
.skill-cols .skill-group{margin-top:1em}
.stamp{display:inline-block;margin:0 0 6px;padding:2px 6px;border:2px solid var(--a1);color:var(--a1);font:700 .72rem var(--mono);letter-spacing:.06em;text-transform:uppercase;transform:rotate(-1.5deg)}
.stamp.s-raftar{transform:none;border-style:double;border-width:4px;padding:1px 6px}
.tags .stamp{display:block;width:max-content;max-width:100%;white-space:nowrap}
@media (max-width:420px){.tags .stamp{white-space:normal}}
.facts div.stamped dd{display:inline-block;border:2px solid var(--a1);color:var(--a1);padding:0 8px;transform:rotate(-1.5deg);font-family:var(--mono);font-size:1rem;text-transform:uppercase;letter-spacing:.04em;font-weight:700}
.broken-fig a.zoom,.broken-fig img{display:none}
.project figure.broken-fig{display:none}
.prose p{margin:0 0 1.1em}
.timeline{margin-top:6px}
.tl-item{padding:16px 0 12px;border-top:1px solid var(--line)}
.tl-item:first-child{border-top:3px solid var(--ink)}
.tl-item .when{margin:0 0 2px;color:var(--a1);font-family:var(--mono);font-size:.82rem;font-weight:500}
.tl-item h3{margin:0}
.tl-item .org{margin:2px 0 8px;color:var(--muted)}
.tl-item p{margin:.25em 0}
.tl-item ul{margin:.4em 0 0;padding-left:1.2em}
.tl-item li{margin:.4em 0}

/* project page: running head, then plain facts */
.proj-hero{max-width:760px;margin:0 auto;padding:28px 20px 8px}
.crumb{display:inline-flex;align-items:center;min-height:44px;margin-bottom:6px;color:var(--fg);font:500 .85rem var(--sans);font-variant:small-caps;letter-spacing:.08em;text-transform:lowercase}
.crumb:hover{color:var(--a1)}
.proj-hero .tags{margin:0 0 10px}
.tldr{font-family:var(--serif);font-size:1.45rem;line-height:1.3;margin:.2em 0 .9em;max-width:30em}
.question{font-size:1rem;color:var(--muted);margin:0;max-width:36em;line-height:1.45}
.question span{font:600 .72rem var(--mono);letter-spacing:.08em;text-transform:uppercase;margin-right:6px}
.facts{display:flex;flex-wrap:wrap;margin:22px 0 28px;padding:0;border-top:3px solid var(--ink);border-bottom:1px solid var(--ink)}
.facts div{flex:1 1 180px;padding:10px 20px 10px 0}
.facts dt{color:var(--muted);font:500 .8rem var(--mono)}
.facts dd{margin:2px 0 0;font-family:var(--serif);font-size:1.2rem;line-height:1.2}
.project h2{margin-top:1.8em;padding-top:.3em;border-top:1px solid var(--line)}
.project figure{margin:1.8em 0}
.project figure img{margin:0 auto;border:1px solid var(--ink)}
.project figure a.zoom{display:block;min-height:44px;cursor:zoom-in}
.project figure.plain img{background:#fff;padding:8px}
.project figure.narrow img{max-width:320px}
.project figure.tall img{max-height:520px;width:auto}
figcaption,.cap{color:var(--muted);font-size:.92rem;text-align:left;margin-top:.7em;line-height:1.5}
.fig-row{display:flex;flex-wrap:wrap;gap:20px;align-items:flex-start;justify-content:center;margin:1.8em 0 .4em}
.fig-row figure{flex:1 1 220px;margin:0}
.project ol,.project ul{padding-left:1.3em}
.pager{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:56px;border-top:3px double var(--ink);padding-top:8px}
.pager a{display:block;padding:12px 8px;text-decoration:none;color:var(--fg);min-height:44px}
.pager a:hover{background:var(--card);box-shadow:inset 0 -3px 0 var(--a1)}
.pager span{display:block;color:var(--a1);font:500 .85rem var(--sans);margin-bottom:2px}
.pager strong{font-family:var(--serif);font-weight:400;font-size:1.15rem;line-height:1.25}
.pager em{display:block;margin-top:4px;color:var(--muted);font-size:.9rem;line-height:1.4;font-style:normal}
.pager .next{text-align:right}

/* footer */
.site-footer{margin-top:40px;border-top:5px double var(--ink);background:var(--band-bg);color:var(--band-fg);padding:28px 0 24px;font-family:var(--sans)}
.footer-inner{max-width:var(--maxw);margin:0 auto;padding:0 20px;display:flex;flex-wrap:wrap;gap:8px 24px;align-items:center;justify-content:space-between}
.footer-inner p{margin:0}
.footer-links{display:flex;flex-wrap:wrap;gap:4px 18px}
.footer-links a{display:inline-flex;align-items:center;min-height:44px;color:var(--band-link);font-weight:500}
.copyright{max-width:var(--maxw);margin:10px auto 0;padding:0 20px;color:var(--band-mute);font-family:var(--mono);font-size:.78rem}

/* lightbox */
.lightbox{position:fixed;inset:0;z-index:200;background:rgba(20,16,12,.94);display:grid;place-items:center;padding:24px;cursor:zoom-out}
.lightbox[hidden]{display:none}
.lightbox img{max-height:90vh;max-width:94vw;background:#fff;border:2px solid #efe7d6}
.lb-close{position:absolute;top:8px;right:12px;width:44px;height:44px;border:0;background:transparent;color:#efe7d6;font-size:2.4rem;cursor:pointer;line-height:1}

@media (prefers-reduced-motion: reduce){
  *{transition:none!important}
  html{scroll-behavior:auto}
}

@media (max-width:860px){
  .intro-grid{grid-template-columns:1fr}
  .about-top,.about-top.no-portrait{grid-template-columns:1fr}
  .about-top.no-portrait .toc{display:none}
  .about-top .portrait{max-width:240px}
  .skill-cols{grid-template-columns:1fr}
}
@media (max-width:620px){
  body{font-size:17px}
  h1{font-size:clamp(2.1rem,10vw,2.7rem)}
  .site-header{gap:6px;padding:4px 12px}
  .brand-name{display:none}
  .site-header nav{flex:1;justify-content:center;gap:0}
  .site-header nav a{padding:0 12px;font-size:.92rem}
  .header-tools a.icon-btn,.hdr-resume{display:none}
  .intro{padding:36px 16px 4px}
  .lede{font-size:1.08rem}
  .section{padding:32px 16px}
  .page-head{padding:32px 16px 8px}
  .proj-hero{padding:20px 16px 4px}
  .row,.row.has-thumb{grid-template-columns:1fr;padding:16px 4px}
  .row.has-thumb{grid-template-columns:80px 1fr}
  .row.has-thumb .thumb{width:80px;height:60px;grid-row:span 2}
  .row.has-thumb .tags{grid-column:2}
  .row.has-thumb.no-thumb{grid-template-columns:1fr}
  .row.has-thumb.no-thumb .tags{grid-column:1}
  .row .no{display:inline;margin-right:8px}
  .pager{grid-template-columns:1fr}
  .pager .next{text-align:left}
  .facts div{flex-basis:100%;padding:8px 0;border-bottom:1px solid var(--line)}
  .facts div:last-child{border-bottom:0}
  .section-head{flex-wrap:wrap}
  .footer-inner{flex-direction:column;align-items:flex-start}
}
"""
with open(os.path.join(OUT, "assets", "style.css"), "w") as f:
    f.write(css.strip() + "\n")

# ----------------------------------------------------------- js
js = r"""
(function(){
  var d=document, root=d.documentElement;

  // theme toggle
  var tb=d.getElementById('theme');
  if(tb){tb.addEventListener('click',function(){
    var cur=root.getAttribute('data-theme');
    if(!cur){cur=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}
    var next=cur==='dark'?'light':'dark';
    root.setAttribute('data-theme',next);
    try{localStorage.setItem('theme',next)}catch(e){}
  });}

  // project filter, with a spoken result count
  var fs=d.querySelectorAll('.filter');
  if(fs.length){
    var rows=d.querySelectorAll('#project-list li'), empty=d.getElementById('empty'), live=d.getElementById('filter-status');
    fs.forEach(function(b){b.addEventListener('click',function(){
      fs.forEach(function(x){x.classList.remove('active');x.setAttribute('aria-pressed','false');});
      b.classList.add('active');b.setAttribute('aria-pressed','true');
      var f=b.getAttribute('data-filter'), shown=0;
      rows.forEach(function(c){
        var ok=f==='all'||(' '+c.getAttribute('data-tags')+' ').indexOf(' '+f+' ')>-1;
        c.hidden=!ok; if(ok){shown++;}
      });
      empty.hidden=shown>0;
      if(live){live.textContent='Showing '+shown+' of '+rows.length+' projects';}
    });});
  }

  // images that fail to load (e.g. a dead hotlink) drop out instead of leaving empty boxes
  function gone(i){var f=i.closest('figure');if(f){f.classList.add('broken-fig');var q=f.previousElementSibling;if(q&&q.tagName==='P'&&/:\s*$/.test(q.textContent)){q.hidden=true;}var r=f.parentNode;if(r&&r.classList.contains('fig-row')&&!r.querySelector('figure:not(.broken-fig)')){r.style.display='none';}}}
  d.querySelectorAll('.about-top .portrait').forEach(function(i){
    function nop(){i.parentNode.classList.add('no-portrait');}
    if(i.complete&&i.naturalWidth===0){nop();}else{i.addEventListener('error',nop);}
  });
  d.querySelectorAll('.row .thumb img').forEach(function(i){
    function nt(){var a=i.closest('.row');if(a){a.classList.add('no-thumb');}}
    if(i.complete&&i.naturalWidth===0){nt();}else{i.addEventListener('error',nt);}
  });
  d.querySelectorAll('.project figure img').forEach(function(i){
    if(i.complete&&i.naturalWidth===0){gone(i);}else{i.addEventListener('error',function(){gone(i);});}
  });

  // Hasselhoff stamp: hold it and the 99 seconds run down. Static for reduced motion; text is restored on release.
  var st=d.querySelector('.facts div.stamped dd');
  if(st&&!(window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches)){
    var orig=st.textContent,tm=null,left=99;
    function stop(){if(tm){clearInterval(tm);tm=null;}st.textContent=orig;left=99;}
    st.addEventListener('pointerdown',function(){if(tm)return;left=99;tm=setInterval(function(){left=Math.max(0,left-1);st.textContent=left+' seconds';if(left===0){clearInterval(tm);tm=null;}},100);});
    ['pointerup','pointerleave','pointercancel'].forEach(function(n){st.addEventListener(n,stop);});
  }

  // image lightbox: figure images are real links to the full image, so they work without JS
  var lb=d.getElementById('lightbox');
  if(lb){
    var lbi=lb.querySelector('img'), closeBtn=lb.querySelector('.lb-close'), opener=null;
    function close(){lb.hidden=true;if(opener){opener.focus();opener=null;}}
    d.addEventListener('click',function(e){
      var a=e.target.closest&&e.target.closest('.project a.zoom');
      if(a){e.preventDefault();opener=a;var im=a.querySelector('img');lbi.src=a.href;lbi.alt=im?im.alt:'';lb.hidden=false;closeBtn.focus();}
      else if(!lb.hidden){close();}
    });
    d.addEventListener('keydown',function(e){
      if(lb.hidden)return;
      if(e.key==='Escape'){close();}
      else if(e.key==='Tab'){e.preventDefault();closeBtn.focus();}
    });
  }
})();
"""
with open(os.path.join(OUT, "assets", "site.js"), "w") as f:
    f.write(js.strip() + "\n")

print("built", len(os.listdir(OUT)), "files in", OUT)
