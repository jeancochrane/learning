;;
;; Define a function `f` that is different when evaluated from left-to-right as
;; right-to-left, e.g.:
;;
;; If left-to-right:
;;      (= 0 (+ (f 0) (f 1)))
;; If right-to-left:
;;      (= 1 (+ (f 0) (f 1)))
;;
(define x 1)

(define (f y) (set! x (* x y)) x)
