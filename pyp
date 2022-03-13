public var show: DodoAnimation {
    switch self {
    case .fade:
      return DodoAnimationsShow.fade
      
    case .noAnimation:
      return DodoAnimations.doNoAnimation
      
    case .rotate:
      return DodoAnimationsShow.rotate
      
    case .slideLeft:
      return DodoAnimationsShow.slideLeft
      
    case .slideRight:
      return DodoAnimationsShow.slideRight
      
    case .slideVertically:
      return DodoAnimationsShow.slideVertically
    }
  }
  
  /**
  
  Get animation function that can be used for hiding notification bar.
  
  - returns: Animation function.
  
  */
  public var hide: DodoAnimation {
    switch self {
    case .fade:
      return DodoAnimationsHide.fade
      
    case .noAnimation:
      return DodoAnimations.doNoAnimation
      
    case .rotate:
      return DodoAnimationsHide.rotate
      
    case .slideLeft:
      return DodoAnimationsHide.slideLeft
      
    case .slideRight:
      return DodoAnimationsHide.slideRight
      
    case .slideVertically:
      return DodoAnimationsHide.slideVertically
    }
  }
