(defun vibe (intensity duration)
  (start-process
   "vibe"
   nil
   "butt.py"
   (number-to-string intensity)
   "--duration" (number-to-string duration)))
