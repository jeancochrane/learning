(define (make-rectangle p q)
  ;;; Make a rectangle from points `p` and `q`
  (cond ((or (= (car p) (car q))
             (= (cadr p) (cadr q)))
          (error make-rectangle
                 "make-rectangle requires two points that are not on a vert or horiz line."
                 p q))
        (else
          (cons p q))))

(define (width rec)
  (let ((p (car rec))
        (q (cdr rec)))
    (abs (- (car p) (car q)))))

(define (height rec)
  (let ((p (car rec))
        (q (cdr rec)))
    (abs (- (cadr p) (cadr q)))))

(define (perimeter rec)
  (+ (* 2 (width rec))
     (* 2 (height rec))))

(define (area rec)
  (* (width rec) (height rec)))
