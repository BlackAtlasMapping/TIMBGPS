# The Insane Math Behind GPS

### About
  Animations for the math portion of "The Insane Math Behind GPS" Video

### Useful commands
  To run an animation:
  ```
  uv run manim -pql main.py CreateCircle
  ```

  To create video from Unreal jpegs:
  ```
    ffmpeg \
    -framerate 60 \
    -start_number 0 \
    -i IntroSequence.%04d.jpeg \
    -c:v libx264 \
    -r 60 \
    -pix_fmt yuv420p \
    IntroSequence.mp4
  ```
