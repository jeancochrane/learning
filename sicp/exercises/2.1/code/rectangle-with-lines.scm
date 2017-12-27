(load "lines.scm")

(define (make-rectangle a width)
  ;;; Make a rectangle from line `a` and a numeric `width`
  (cond ((<= width 0)
          (error make-rectangle
                 "Rectangles must have a width >0. Your width:"
                 width))
        (else
          (cons a width))))

(define (width rec)
  (cdr rec))

(define (height rec)
  (let ((a (car rec)))
    (sqrt (+ (square (- (x-point (start-segment a))
                        (x-point (end-segment a))))
             (square (- (y-point (start-segment a))
                        (y-point (end-segment a))))))))

(define (perimeter rec)
  (+ (* 2 (width rec))
     (* 2 (height rec))))

(define (area rec)
  (* (width rec) (height rec)))
