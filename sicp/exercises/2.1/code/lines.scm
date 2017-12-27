(define (print-point p)
  ;;; Print a point `p` on the coordinate plane
  (newline)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")"))

(define make-segment
  ;;; Constructor procedure that takes two points and returns a line segment
  cons)

(define start-segment
  ;;; Selector procedure that takes a line segment and returns its initial point
  car)

(define end-segment
  ;;; Selector procedure that takes a line segment and returns its endpoint
  cdr)

(define make-point cons)

(define x-point car)

(define y-point cdr)

(define (average x y)
  (/ (+ x y) 2))

(define (midpoint-segment s)
  ;;; Find the midpoint of a line segment `s`.
  (make-point (average (x-point (start-segment s))
                       (x-point (end-segment s)))
              (average (y-point (start-segment s))
                       (y-point (end-segment s)))))
