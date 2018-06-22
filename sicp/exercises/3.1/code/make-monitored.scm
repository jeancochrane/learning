(define (make-monitored f)
  ;;;
  ;;; Monitor the procedure `f`, allowing the user to inspect
  ;;; the number of times that it is called in a given procedure.
  ;;;
  (define counter 0)
  (define (mf arg)
    (cond ((eq? arg 'how-many-calls?)
            counter)
          ((eq? arg 'reset-count)
            (set! counter 0)
            (counter))
          (else
            (set! counter (+ counter 1))
            (f arg))))
    mf)
