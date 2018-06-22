(define (make-accumulator init)
  (lambda (x)
    (set! init (+ init x))
    init))

; Test
(let ((A (make-accumulator 5)))
  (A 10))
; Expected: 15
