import { formatPrice, type MenuItem } from "../data/menu";

type Props = { item: MenuItem; feature?: boolean; compact?: boolean };

export default function MenuCard({ item, feature = false, compact = false }: Props) {
  return (
    <article className={`mcard ${feature ? "mcard--feature" : ""} ${compact ? "mcard--compact" : ""}`.trim()} data-swap>
      <div className="mcard__media">
        <img src={item.image} alt={item.name} width={800} height={1000} loading="lazy" decoding="async" />
      </div>
      <div className="mcard__body">
        {feature && <p className="mcard__flag">House signature</p>}
        <h3 className="mcard__row">
          <span className="mcard__name">{item.name}</span>
          <span className="mcard__leader" aria-hidden="true" />
          <span className="mcard__price">{formatPrice(item.price)}</span>
        </h3>
        <p className="mcard__desc">{item.description}</p>
      </div>
    </article>
  );
}
